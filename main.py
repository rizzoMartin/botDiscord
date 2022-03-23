import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands

class MyClient(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Connection
    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged on as {0}! (id: {1})'.format(self.bot.user, self.bot.user.id))

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot has reconnected!')

    # handle errors
    @commands.Cog.listener()
    async def on_command_errror(self, ctx, error):
        await ctx.send(error)

# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# bot prefix
bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'),
                   description='Un bot de prueba', 
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
            except:
                print(f'an error ocurred loading the extension {cog}')

    bot.add_cog(MyClient(bot))
    bot.run(token, reconnect=True)