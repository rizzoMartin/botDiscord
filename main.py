import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands

# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

descripction='Bot de musica sencillo'

# bot prefix
bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'),
                   description=description, 
                   intents=intents)

# logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='UTF-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Load data from .env file
load_dotenv()
token = os.getenv('TOKEN')

if __name__ == '__main__':
    # load extensions
    for cog in os.listdir('./cogs'):
        if cog.endswith('.py'):
            try:
                bot.load_extension(f'cogs.{cog[: -3]}')
            except Exception as e:
                print(f'an error ocurred loading the extension {cog}: {e}')

    bot.run(token, reconnect=True)