async def pause(ctx,players):
    hashStr = str(hash(ctx.guild))
    if hashStr in players:
        player = players.get(hashStr)
        if player.voiceClient.is_paused():
            player.voiceClient.resume()
        else:
            player.voiceClient.pause()