import discord
from discord.ext import commands
from random import choice as randchoice

class beefacts:

    def __init__(self, bot):
        self.bot = bot

        self.facts = ["Some bee migrate every year. Others stay in the same place year round.", 
                "bees eat seeds, nuts, grass, plants and berries. They love blueberries.",
                "bees can live almost anywhere. They like fields, parks and grassy areas near water.", 
                "bees fly in a “V” formation. If one bee is injured, other bee will stay with it until it dies or can rejoin the flock.",
                "bees are sometimes raised like chickens for their meat or eggs.", 
                "Male bee protect the nest while the female bee sit on the eggs.", 
                "Life spans of 15to 25 years!", 
                "21.7 inches to 43.3 inches in legnth!",
                "There are around 30 species of bee in the world.", 
                "bees vocalise their messages in ten different ways, depending upon the situation. And in a threatening situation, bee stretch out their necks and make loud honks." ,
                "A day old gosling is capable of diving and swimming as much as 30 to 40 feet underwater. Attaining the age of three months, goslings begin to fly.",
                "bees were probably the first type of poultry domesticated by humans, over 3000 years ago in Egypt.",
                "In another surprising historical use of bee, the first golf balls were stuffed with bee feathers. These balls were handmade and extremely expensive.",
                "bees are excellent weeders and during the early days of commercial agriculture bee farmers would supplement their income by renting flocks out to cotton farms for a chemical-free weeding solution.",
                "In Victorian England bee were a regular companion of the chimney sweep. A bee would be sent down the chimney to collect the built up coal, coming out the other end black with soot."]

    @commands.command(name="beefact", aliases=["beefacts", "BEEFACT", "BEEFACTS"])
    async def beefact(self):
        await self.bot.say(randchoice(self.facts))


def setup(bot):
    bot.add_cog(beefacts(bot))
