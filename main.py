import asyncio
import discord
from supabase import create_client, Client

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Supabase setup
url = ""
key = ""
supabase: Client = create_client(url, key)

async def update_lab_status():
    while True:
        try:
            response = supabase.table("Door Status").select("*").order('created_at', desc=True).execute()
            if response.data:
                door_status = response.data[0]
                
                channel_id = 1285685359107379260
                channel = client.get_channel(channel_id)
                
                if channel is None:
                    print(f"Channel with ID {channel_id} not found.")
                    return
                
                if door_status['is_open']:
                    new_name = 'Lab Status: Open'
                else:
                    new_name = 'Lab Status: Closed'
                
                if channel.name != new_name:
                    await channel.edit(name=new_name)
                    print(f"Channel name updated to: {new_name}")
            else:
                print("No data found in Supabase.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

        await asyncio.sleep(300)  # Sleep for 5 minutes

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Start the background task
    client.loop.create_task(update_lab_status())

# Run the bot
client.run("")
