from dotenv import load_dotenv
from command.__init__ import *
from events.__init__ import *
from command.music.__init__ import *
import discord
import sys

f = open(os.path.abspath(os.getcwd()) + '/config.json')
config = json.load(f)
f.close()

type = sys.argv[1]
load_dotenv()
ENV_VAR = os.environ
TOKEN = ENV_VAR[(config[type]["token"])]

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)

events = Events(client, config[type], ENV_VAR)
command = Commands(client, config[type], ENV_VAR)
music = Music(client, config, ENV_VAR)

client.add_cog(events)
client.add_cog(command)
client.add_cog(music)

client.run(TOKEN)