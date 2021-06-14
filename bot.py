from dotenv import load_dotenv
import os

from commands.__init__ import init_commands
from events.__init__ import *
import discord

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!',intents=intents)

init_commands(client)
client.add_cog(Events(client))

client.run(TOKEN)

