import discord

async def queue(ctx,players):
    hashStr = str(hash(ctx.guild))
    if hashStr in players:
        player = players.get(hashStr)
        list = ""
        index = 0
        for entry in player.queue:
            list += "**" + str(index) +"**: " + entry.title +"\n"
            index += + 1

        embedVar = discord.Embed(title="Nuvarande kö:", description=list, color=0xfa6607)
        await player.tchannel.send(embed=embedVar)