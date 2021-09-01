import discord
from discord.ext import commands
from command.helpers import retrieveCourse


async def stats(ctx, course):
    json = retrieveCourse(course)
    if len(json) == 0:
        await ctx.channel.send("Hittade inte den kursen :(")
        return

    total = 0
    totalfailrate = 0
    for entry in json:
        failed = entry.get('failed')
        passed = entry.get('three') + entry.get('four') + entry.get('five')
        totalfailrate += (failed / (passed + failed)) * 100
        total += failed + passed
    rate = totalfailrate / len(json)

    for entry in json:
        u = entry.get('failed')
        three = entry.get('three')
        four = entry.get('four')
        five = entry.get('five')
        if (u + three + four + five > total / len(json) + 20):
            break

    embedVar = discord.Embed(title="Statistik", description=course.upper(), color=0xfa6607)
    embedVar.add_field(name="Failrate", value="Den genomsnittliga failraten ligger på: **" + str(
        round(rate, 2)) + "%**.", inline=False)
    embedVar.add_field(name="Senaste ordinarie tentan", value="Tentan " + entry.get('date') + " hade följande betygsfördelning: \n**U**: " + str(u) + "\n**3**: "
                                                              + str(three) + "\n" + "**4**: " + str(four) + "\n**5**: " + str(five), inline=False)
    embedVar.add_field(name="Länk till tenta.davebay", value = "https://tenta.davebay.net/course/" + course)
    await ctx.channel.send(embed=embedVar)
