import discord
import time
from discord.ext import commands
import random
import webbrowser
import setproctitle

setproctitle.setproctitle('')


client = commands.Bot(command_prefix = ';', self_bot=True)
token = input('Token: ')
clname = input('Name Of Stream: ')
print('twitch URL must start with https://')
clurl = input('Your Twitch : ')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=clname, url=clurl))
setproctitle.setproctitle(f'Logged in as {client.User}')

client.run(token, bot=False)
