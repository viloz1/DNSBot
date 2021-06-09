from dotenv import load_dotenv
import os

import discord
import ast
from discord.ext import commands
from asyncio import *
from events import *
import requests
import json
from commands.__init__ import init_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!',intents=intents)

init_commands(client)

@client.event
async def on_ready():
    print("Ready!")

@client.event
async def on_message(message):
    await client.process_commands(message)
    await on_messageEvent(message)

client.run(TOKEN)

