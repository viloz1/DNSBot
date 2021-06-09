from commands.coursespecific.betyg import *
from commands.coursespecific.failrate import *
import discord
from asyncio import *

def init_commands(client):
    client.add_command(failrate)
    client.add_command(betyg)
