from dotenv import load_dotenv
import os
import json
import sys
import subprocess

from command.__init__ import *
from events.__init__ import *
import discord

def main(type):
    f = open(os.path.abspath(os.getcwd()) + '/config.json')
    config = json.load(f)
    f.close()

    load_dotenv()
    TOKEN = os.getenv(config[type]["token"])

    intents = discord.Intents.default()
    intents.members = True
    client = commands.Bot(command_prefix='!', intents=intents)

    events = Events(client,config[type])
    command = Commands(client,config[type])
    client.add_cog(events)
    client.add_cog(command)

    client.run(TOKEN)

