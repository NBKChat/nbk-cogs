import discord
import datetime
from discord.ext import commands

class countdown:

    def __init__(self, bot):
        self.bot = bot

    delta = datetime.datetime(2018, 10, 29) - datetime.datetime.now()
    @commands.command(name="jamcountdown", aliases=["jamcount", "jamtimer", "jamtime"])

    async def beefact(self):
        await self.bot.say(delta.days)


def setup(bot):
    bot.add_cog(countdown(bot))
