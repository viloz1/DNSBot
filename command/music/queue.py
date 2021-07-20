import discord

async def queue(ctx,players):
    hashStr = str(hash(ctx.guild))
    if hashStr in players:
        player = players.get(hashStr)
        list = "**0**: "+player.lastSong.title+" **<-- Nuvarande låt** \n"
        index = 1
        for entry in player.queue:
            list += "**" + str(index) +"**: " + entry.title +"\n"
            index += + 1

        embedVar = discord.Embed(title="Nuvarande kö:", description=list, color=0xfa6607)
        await player.tchannel.send(embed=embedVar)
    else:
        await ctx.channel.send("Hur har du tänkt att se kön på något som inte finns?")