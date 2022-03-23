from discord.ext import commands

class Listeners(commands.Cog):
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

def setup(bot):
    bot.add_cog(Listeners(bot))