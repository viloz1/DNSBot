import discord

from events.onMessageEvents.random import *
from events.onMessageEvents.anonymousMsg import *

async def on_message_handler(config, message,client):

    if message.author == client.user:
        return

    if isinstance(message.channel, discord.channel.DMChannel):
        await anonymousMsg(message, client, config["channels"]["anonymous_message"])
        return

    if message.channel.id == config["channels"]["anonymous_message"]:
        await anonymousAnsw(message, client, config["channels"]["anonymous_message"])
        return

    await random(message)

