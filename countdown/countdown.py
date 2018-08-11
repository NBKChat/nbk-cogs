import discord
import datetime
from discord.ext import commands

class countdown:

    def __init__(self, bot):
        self.bot = bot
        self.delta = datetime.datetime(2018, 10, 29) - datetime.datetime.now()
        self.output = "{} days {} hours {} minutes until the jam".format(self.delta.days, self.delta.seconds//3600, (self.delta.seconds//60)%60)

    @commands.command(name="jamcountdown", aliases=["jamcount", "jamtimer", "jamtime"])

    async def countdown(self):
        await self.bot.say(self.output)


def setup(bot):
    bot.add_cog(countdown(bot))
