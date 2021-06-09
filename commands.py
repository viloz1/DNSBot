import os
import discord
import requests
from asyncio import *

def init_commands(client):
    @client.command(pass_context=True)
    async def failrate(ctx, course):
        totalfailrate = 0
        URL = "https://tenta.davebay.net/api/course/" + course + "/exams"
        request = requests.get(url = URL)
        json = request.json()
        if len(json) == 0:
            await ctx.channel.send("Hittade inte den kursen :(")
            return
        for entry in json:
            failed = entry.get('failed')
            passed = entry.get('three') + entry.get('four') + entry.get('five')
            totalfailrate += (failed / (passed + failed)) * 100
        rate = totalfailrate / len(json)
        await ctx.channel.send("**" + course.upper() + "**" + " har en genomsnittlig failrate på: " + "**" + str(round(rate, 2)) + "%**.")


