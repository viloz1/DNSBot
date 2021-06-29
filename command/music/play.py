from command.music.downloadYT import download
from command.music.__init__ import Player

async def play(ctx, url, players):
    hashStr = str(hash(ctx.guild))
    pathAndTitle = await download(url)
    if hashStr in players:
        player = players.get(hashStr)
        player.addEntry(pathAndTitle[0],pathAndTitle[1])
    else:
        voice = await ctx.author.voice.channel.connect()
        channel = ctx.author.voice.channel
        player = Player(channel, voice, ctx.channel)
        player.addEntry(pathAndTitle[0],pathAndTitle[1])
        players.update({str(hash(ctx.guild)): player})


