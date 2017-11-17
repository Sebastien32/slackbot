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

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

@client.event
async def on_message(message):
    msg = message.content.lower().split(' ')
    if message.author != client.user:
        if msg[0] == '!roll':
            if len(msg) > 1 and RepresentsInt(msg[1]):
                if (len(msg[1]) > 9):
                    await client.send_message(message.channel, '{0.author.mention} rolls '.format(message) + str(random.randint(0, 100)) + ' point(s)')
                elif int(msg[1]) >= 0:
                    if message.author == 'Sebastien Whetsel':
                        await client.send_message(message.channel, '{0.author.mention} rolls '.format(message) + str(msg[1]) + ' point(s)')
                    else:
                        await client.send_message(message.channel, '{0.author.mention} rolls '.format(message) + str(random.randint(0, int(msg[1]))) + ' point(s)')
            else:
                await client.send_message(message.channel, '{0.author.mention} rolls '.format(message) + str(random.randint(0, 100)) + ' point(s)')
        elif msg[0] == '!help':
            await client.send_message(message.channel, '```!roll - Rolls random number between 0 and 100\n\n' +
                '!roll # - Rolls random number between 0 and # (if # has more than 9 digits, rolls default)\n\n' +
                '"bomb", "potassium nitrate", "motor", or "ammonium perchlorate" - Says "You have been added to the F.B.I. watchlist."\n\n' +
                '"motor" - Says "whoosh"```')
        elif msg[0] == '!death':
            await client.send_message(message.channel, 'RIP {0.author.mention}, who has now ded in piece'.format(message))
        else:
            msg = message.content.lower()
            if 'potassium nitrate' in msg or 'bomb' in msg or 'ammonium perchlorate' in msg:
                await client.send_message(message.channel, 'You have been added to the F.B.I. watchlist.')
            elif 'motor' in msg:
                await client.send_message(message.channel, 'whoosh')
            elif 'launch' in msg:
                await client.send_message(message.channel, 'lunch')

client.run('MzM5Mjk2OTczODc2MzYzMjc1.DFiCcw.4BbB6zWCbfJcXQVy9gTJJMY88Zg')
