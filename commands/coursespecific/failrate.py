import os
import discord
from discord.ext import commands
import requests
from asyncio import *
from commands.helpers import retrieveCourse

@commands.command()
async def failrate(ctx, course):
    totalfailrate = 0
    json = retrieveCourse(course)
    if len(json) == 0:
        await ctx.channel.send("Hittade inte den kursen :(")
        return
    for entry in json:
        failed = entry.get('failed')
        passed = entry.get('three') + entry.get('four') + entry.get('five')
        totalfailrate += (failed / (passed + failed)) * 100
    rate = totalfailrate / len(json)
    await ctx.channel.send("**" + course.upper() + "**" + " har en genomsnittlig failrate på: " + "**" + str(round(rate, 2)) + "%**.")
