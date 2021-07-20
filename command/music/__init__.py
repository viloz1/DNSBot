from discord.ext import commands, tasks
import command.music.play
import command.music.stop
import command.music.pause
import command.music.skip
import command.music.queue
import command.music.clear
import command.music.helpers as helpers
import time
import discord
import os


class QueueEntry:
    def __init__(self, path = "", title= "", id= ""):
        self.path = path
        self.title = title
        self.id = id

class Player:
    def __init__(self, channel, voiceClient, textChannel):
        self.channel = channel
        self.voiceClient = voiceClient
        self.tchannel = textChannel

    queue = list()
    isStopped = False
    voiceClient = discord.VoiceClient
    channel = discord.VoiceChannel
    tchannel = discord.TextChannel
    lastSong = QueueEntry()

    def addEntry(self, path, title, id):
        entry = QueueEntry(path, title, id)
        self.queue.append(entry)

class Music(commands.Cog):
    def __init__(self, bot, config, env):
        self.bot = bot
        self.config = config
        self.env = env
        self.musicEventLoop.start()
        self.clearCache.start()

    players = {}
    env = dict

    @tasks.loop(minutes=10)
    async def clearCache(self):
        print("Clearing cache...")
        cache = helpers.getCache(self.env)
        for id, lastPlayed in cache.items():
            if time.time() - lastPlayed > 172800:  # 48h
                try:
                    print("Removing temp/" + id + ".opus")
                    os.remove("temp/" + id + ".opus")
                except:
                    print("Error: can't remove id " + id)
                    pass
        print("Cache cleared!")

    @tasks.loop(seconds=2)
    async def musicEventLoop(self):
        deleteList = []
        for hash, player in self.players.items():
            if not player.voiceClient.is_playing() and not player.voiceClient.is_paused():
                if len(player.queue) > 0 and not player.isStopped:
                    track = player.queue.pop(0)
                    helpers.updateEntry(track.id, self.env)
                    player.lastSong = track
                    embedVar = discord.Embed(title="Spelar nu:", description=track.title, color=0xfa6607)
                    await player.tchannel.send(embed=embedVar)
                    player.voiceClient.play(discord.FFmpegPCMAudio(track.path))
                    player.voiceClient.source = discord.PCMVolumeTransformer(player.voiceClient.source, 1)
                else:
                    deleteList.append(hash)
                    await player.voiceClient.disconnect()

        for entry in deleteList:
            del self.players[entry]


    @commands.command()
    async def play(self, ctx, url):
        await command.music.play.play(ctx, url, self.players, self.env)

    @commands.command()
    async def stop(self, ctx):
        await command.music.stop.stop(ctx, self.players)

    @commands.command()
    async def pause(self, ctx):
        await command.music.pause.pause(ctx, self.players)

    @commands.command()
    async def skip(self, ctx, *, arg=[]):
        await command.music.skip.skip(ctx, self.players, arg)

    @commands.command()
    async def queue(self, ctx):
        await command.music.queue.queue(ctx, self.players)

    @commands.command()
    async def clear (self, ctx):
        await command.music.clear.clear(ctx, self.players)