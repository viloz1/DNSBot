from dotenv import load_dotenv
import os
import discord
import ast
from discord.ext import commands
from asyncio import *
from commands import *
import requests
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!',intents=intents)

init_commands(client)

@client.event
async def on_ready():
    print("Ready!")

client.run(TOKEN)

