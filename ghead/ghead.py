
from discord.ext import commands

class Ghead:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ghead(self, head):

        await self.bot.say("http://whiskeycrow.com/Graal/heads/" + head + ".png")

def setup(bot):
    bot.add_cog(Ghead(bot))
