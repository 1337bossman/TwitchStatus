import discord
import time
from discord.ext import commands
import random

client = commands.Bot(command_prefix = ';', self_bot=True)
token = input('Token: ')
clname = input('Name Of Stream: ')
print('twitch URL must start with https://')
clurl = input('Your Twitch : ')
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name=clname, url=clurl))


client.run(token, bot=False)
