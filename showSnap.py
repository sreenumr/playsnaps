import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from Crossword import Crossword

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.default()
# intents.message_content = True
# bot = discord.Client(intents=intents)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

alphabet_emojis = {
'a': '\U0001F1E6',
    'b': '\U0001F1E7',
    'c': '\U0001F1E8',
    'd': '\U0001F1E9',
    'e': '\U0001F1EA',
    'f': '\U0001F1EB',
    'g': '\U0001F1EC',
    'h': '\U0001F1ED',
    'i': '\U0001F1EE',
    'j': '\U0001F1EF',
    'k': '\U0001F1F0',
    'l': '\U0001F1F1',
    'm': '\U0001F1F2',
    'n': '\U0001F1F3',
    'o': '\U0001F1F4',
    'p': '\U0001F1F5',
    'q': '\U0001F1F6',
    'r': '\U0001F1F7',
    's': '\U0001F1F8',
    't': '\U0001F1F9',
    'u': '\U0001F1FA',
    'v': '\U0001F1FB',
    'w': '\U0001F1FC',
    'x': '\U0001F1FD',
    'y': '\U0001F1FE',
    'z': '\U0001F1FF'
}


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')



# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')
#     await bot.process_commands(message)

@bot.command()
async def play(ctx):
    channels = bot.get_all_channels()
    voiceChannels = []

    await ctx.send(' '.join(alphabet_emojis.values()))

crossword = Crossword()
crossword.generate_crossword()
# bot.run(TOKEN)