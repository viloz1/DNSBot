import discord
from asyncio import *

def init_events(client):
    @client.event
    async def on_message(message):
        if message.content.lower() == "sköj":
            await message.channel.send("***skôj***")
