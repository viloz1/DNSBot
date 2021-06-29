from discord.ext import commands, tasks
import command.music.play
import command.music.stop
import command.music.pause
import command.music.skip
import command.music.queue
import discord
import asyncio
import os

class Player:
    def __init__(self, channel, voiceClient, textChannel):
        self.channel = channel
        self.voiceClient = voiceClient
        self.tchannel = textChannel

    queue = list()
    voiceClient = discord.VoiceClient
    channel = discord.VoiceChannel
    tchannel = discord.TextChannel
    lastSong = ""

    class QueueEntry:
        def __init__(self, path, title):
            self.path = path
            self.title = title

        path = ""
        title = ""

    def addEntry(self, path, title):
        entry = self.QueueEntry(path, title)
        self.queue.append(entry)

class Music(commands.Cog):
    def __init__(self, bot, config, players):
        self.bot = bot
        self.config = config
        self.players = players
        self.musicEventLoop.start()

    players = dict

    @tasks.loop(seconds=2)
    async def musicEventLoop(self):
        deleteList = []
        for hash, player in self.players.items():
            if not player.voiceClient.is_playing() and not player.voiceClient.is_paused():
                if not len(player.queue) == 0:
                    if player.lastSong != "":
                        os.remove(player.lastSong)
                    track = player.queue.pop(0)
                    path = track.path
                    player.lastSong = path
                    embedVar = discord.Embed(title="Spelar nu:", description=track.title, color=0xfa6607)
                    await player.tchannel.send(embed=embedVar)
                    player.voiceClient.play(discord.FFmpegPCMAudio(path))
                    player.voiceClient.source = discord.PCMVolumeTransformer(player.voiceClient.source, 1)
                else:
                    deleteList.append(hash)
                    await player.voiceClient.disconnect()

        for hash in deleteList:
            os.remove(self.players[hash].lastSong)
            del self.players[hash]

    @commands.command()
    async def play(self, ctx, url):
        await command.music.play.play(ctx, url, self.players)

    @commands.command()
    async def stop(self,ctx):
        await command.music.stop.stop(ctx, self.players)

    @commands.command()
    async def pause(self, ctx):
        await command.music.pause.pause(ctx, self.players)

    @commands.command()
    async def skip(self, ctx):
        await command.music.skip.skip(ctx, self.players)

    @commands.command()
    async def queue(self, ctx):
        await command.music.queue.queue(ctx, self.players)