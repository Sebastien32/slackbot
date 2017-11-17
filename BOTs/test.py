import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('BOT is online!')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('------')

# @bot.event
# async def on_message(message):
#     msg = message.content.lower()
#     if 'potassium nitrate' in msg or 'bomb' in msg:
#         return await bot.say('You have been added to the F.B.I. watchlist.')

@bot.command()
async def roll(*args):
    if len(args) == 0:
        return await bot.say(('{0.name} rolls ' + str(random.randint(1, 100)) + ' point(s)').format(discord.Member))

bot.run('MzM5Mjk2OTczODc2MzYzMjc1.DFiCcw.4BbB6zWCbfJcXQVy9gTJJMY88Zg')
