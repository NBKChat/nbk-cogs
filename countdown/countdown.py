import discord
import datetime
from discord.ext import commands

class countdown:

    def __init__(self, bot):
        self.bot = bot
        self.jamtime = datetime.datetime(2018, 10, 29)

    def countdownout(self):
        delta = self.jamtime - datetime.datetime.now()
        return "{} days {} hours {} minutes until the jam".format(delta.days, delta.seconds//3600, (delta.seconds//60)%60)

    @commands.command(name="jamcountdown", aliases=["jamcount", "jamtimer", "jamtime"])

    async def countdown(self):
        await self.bot.say(countdownout())


def setup(bot):
    bot.add_cog(countdown(bot))
