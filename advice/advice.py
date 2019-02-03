from discord.ext import commands
import requests
import json

class Advice:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def advice(self):
        response = requests.get("https://api.adviceslip.com/advice")
        responseJson = response.json()
        slip = responseJson['slip']
        advice = slip['advice']
        await self.bot.say(advice)
        

def setup(bot):
    bot.add_cog(Advice(bot))
