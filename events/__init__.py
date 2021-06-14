from events.onMessageEvents.__init__ import *
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await on_message_handler(message, self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready!")