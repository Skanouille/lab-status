from typing import Final
import os
import discord
import time, asyncio
from pymongo import MongoClient

# fetch from database
def get_database():
    # fill in mongodb atlas url to connect using pymongo
    CONNECTION_STRING =
""
    client = MongoClient(CONNECTION_STRING)
    return client['lab status']

    # for files to reuse function get_database()
if __name__ == "__main__":

    dbname = get_database()
 
# change lab status to OPEN
@client.event
async def
    channel = client.get_channel("751662000093921291")
    await channel.edit(name = 'Lab Status: Open')

# change lab status to CLOSED
async def
    channel = client.get_channel("751662000093921291")
    await channel.edit(name = 'Lab Status: Closed')