from events.onMessageEvents.__init__ import *
from discord.ext import commands
from command.music.__init__ import *

class Events(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config

    @commands.Cog.listener()
    async def on_message(self, message):
        await on_message_handler(self.config, message, self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")

