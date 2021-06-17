import discord
import os
import random


async def seal(ctx):
    PATH = os.getenv('DB_PATH') + "/pictures/seals"
    rand = random.randrange(0, len(os.listdir(PATH)))
    await ctx.channel.send(file=discord.File(PATH + "/seal" + str(rand) + ".jpg"))
