from command.music.downloadYT import download
from command.music.__init__ import Player
import asyncio


async def play(ctx, url, players, env):
    hashStr = str(hash(ctx.guild))
    info = await download(url, env)
    if hashStr in players:
        player = players.get(hashStr)
        player.addEntry(info['path'], info['title'], info['id'])
    else:
        try:
            voice = await ctx.author.voice.channel.connect()
        except:
            pass
        channel = ctx.author.voice.channel
        try:
            player = Player(channel, voice, ctx.channel)
        except:
            i = 0
            while players.get(hashStr) == None:
                await asyncio.sleep(1)
                if i >= 5:
                    await ctx.channel.send("Whoops, något gick fel. Videon **" + info["title"] + "** kunde inte läggas till i kön.")
                    return
                i = i + 1
            player = players.get(hashStr)
        player.addEntry(info['path'], info['title'], info['id'])
        players.update({str(hash(ctx.guild)): player})
