import discord

from events.onMessageEvents.skoj import *
from events.onMessageEvents.anonymousMsg import *

async def on_message_handler(message,client):
    if message.author == client.user:
        return

    DB_PATH = os.getenv("DB_PATH")
    f = open(DB_PATH + "\config.json")
    config = json.load(f)
    f.close()

    if isinstance(message.channel, discord.channel.DMChannel):
        await anonymousMsg(message, client)
        return

    if message.channel.id == config["channels"]["anonymous_messages"]:
        await anonymousAnsw(message, client)
        return

    await skoj(message)