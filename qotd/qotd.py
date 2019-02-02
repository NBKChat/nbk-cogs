from discord.ext import commands
import requests
import json

class Qotd:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()

    async def qotd(self):
        response = requests.get("http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")
        responseJson = json.loads(response.text)
        author = responseJson['quoteAuthor']
        quote = responseJson['quoteText']
        if author == "":
            author = "Anonymous"
        await self.bot.say(quote)
        await self.bot.say("- " + author)

def setup(bot):
    bot.add_cog(Qotd(bot))
