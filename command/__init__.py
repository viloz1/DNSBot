import command.coursespecific.stats
import command.random.seal
from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot, config, env):
        self.bot = bot
        self.env = env
        self.config = config

    @commands.command()
    async def seal(self,ctx):
        await command.random.seal.seal(ctx)

    @commands.command()
    async def stats(self,ctx,course):
        await command.coursespecific.stats.stats(ctx, course)
