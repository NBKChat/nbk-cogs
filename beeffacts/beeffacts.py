import discord
from discord.ext import commands
from random import choice as randchoice

class beeffacts:

    def __init__(self, bot):
        self.bot = bot

        self.facts = [
            "Every day, 76 million Americans eat beef.",
            "Beef is meat from full-grown cattle about 2 years old.",
            "A live steer weighs about 1,000 pounds and yields about 450 pounds of edible meat.",
            "More beef is consumed on Memorial Day than any other day of the year. The Fourth of July and Labor Day typically tie for second place.",
            "Beef is one of the most important dietary sources of iron. To obtain the same amount of iron found in a 3-ounce serving of beef, you’d have to eat at least 3 cups of raw spinach.",
            "There are more than 800,000 ranchers and cattle producers in the United States.",
            "More than 97 percent of beef cattle farms and ranches are classified as family farms."
        ]

    @commands.command(name="beeffact", aliases=["beeffacts", "BEEFFACT", "BEEFFACTS"])
    async def beeffact(self):
        await self.bot.say(randchoice(self.facts))


def setup(bot):
    bot.add_cog(beeffacts(bot))
