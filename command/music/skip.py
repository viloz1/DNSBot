async def skip(ctx, players, arguments):
    hashStr = str(hash(ctx.guild))
    if hashStr in players:
        player = players.get(hashStr)
        if player.voiceClient.is_paused():
            player.voiceClient.resume()
        if arguments != []:
            try:
                player.queue = player.queue[int(arguments[0])-1:]
            except:
                ctx.channel.send("Det där är inget nummer :(")
        player.voiceClient.stop()
    else:
        await ctx.channel.send("Hur har du tänkt att skippa något som inte finns?")