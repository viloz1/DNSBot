from events.onMessageEvents.__init__ import *
from command.music.__init__ import *
from events.mainMessage import *
from events.errorHandlers import *

class Events(commands.Cog):
    def __init__(self, bot, config, env):
        self.bot = bot
        self.config = config
        self.env = env

    @commands.Cog.listener()
    async def on_message(self, message):
        await on_message_handler(self.config, message, self.bot)

    @commands.Cog.listener()
    async def on_ready(self):
        await mainMessage(self)

        print("Ready!")
    


