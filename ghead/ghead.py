from discord.ext import commands
from bs4 import BeautifulSoup
import requests

class Ghead:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ghead(self, head):

        url = 'http://whiskeycrow.com/Graal/heads/'
        ext = 'png'
        match_string = True
        def list_dir(url, ext=''):
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'html.parser')
            return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

        for file in list_dir(url, ext):
            if head + ".png" == file:
                await self.bot.say("http://whiskeycrow.com/Graal/heads/" + head + ".png")
            else:
                match_string = False
        if match_string == False: await self.bot.say(head + " not found, noob")

def setup(bot):
    bot.add_cog(Ghead(bot))
