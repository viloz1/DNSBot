import os
import discord
from discord.ext import commands
import requests
from asyncio import *
from commands.helpers import *

@commands.command()
async def betyg(ctx, course):
    json = retrieveCourse(course)
    if len(json) == 0:
        await ctx.channel.send("Hittade inte den kursen :(")
        return
    for i in range(len(json) - 1, -1, -1):
        entry = json[i]
        u = entry.get('failed')
        three = entry.get('three')
        four = entry.get('four')
        five = entry.get('five')
        total = u + three + four + five
        if isOrdinarieTenta(json, total):
            await ctx.channel.send("Senaste ordinarie tenta (" + entry.get('date') + ") hade följande betygsfördelning: \n**U**: " + str(u) + "\n" +
                                 "**3**: " + str(three) + "\n" + "**4**: " + str(four) + "\n" + "**5**: " + str(five))
            return
