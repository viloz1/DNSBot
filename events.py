import discord
from asyncio import *

async def on_messageEvent(message):
    if message.content.lower() == "sköj":
        await message.channel.send("***skôj***")
        return
