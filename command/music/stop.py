import discord

async def stop(ctx,players):
    hashStr = str(hash(ctx.guild))
    if hashStr in players:
        player = players.get(hashStr)
        player.queue = []
        player.voiceClient.stop()