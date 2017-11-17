import discord
from discord.ext import commands
import random

client = discord.Client()

@client.event
async def on_ready():
    print('BOT is online!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author != client.user:
        await client.send_message(message.channel, 'durr hurr')

client.run('MzM5NTQ3NTc5NjIyNzUyMjU3.DFlj3g.84geT0uvBXs7mMVpz4S5_CMPEjg')
