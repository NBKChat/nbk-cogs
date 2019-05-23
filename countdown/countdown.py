import discord
import datetime
from discord.ext import commands

class countdown:

    def __init__(self, bot):
        self.bot = bot
        self.jamtime = datetime.datetime(2019, 6, 15)

    @commands.command(name="jamcountdown", aliases=["jamcount", "jamtimer", "jamtime", "sharkweek"])

    async def countdown(self):
        delta = self.jamtime - datetime.datetime.now()
        if delta.days < 0:
            output = "its jamtime decision time"
        else:
            output =  "{} days {} hours {} minutes until shark week".format(delta.days, delta.seconds//3600, (delta.seconds//60)%60)
        await self.bot.say(output)


def setup(bot):
    bot.add_cog(countdown(bot))
