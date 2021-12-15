from discord.ext import commands


class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name ='oi')
    async def send_hello(self, ctx):
        response = "Olá"

        await ctx.send(response)


def setup(bot):
    bot.add_cog(Talks(bot))
