

async def stop(ctx,players):
    hashStr = str(hash(ctx.guild))
    if hashStr in players:
        player = players.get(hashStr)
        player.voiceClient.stop()
        player.isStopped = True
    else:
        await ctx.channel.send("Hur har du tänkt att stoppa något som inte finns?")