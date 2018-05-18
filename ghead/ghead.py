from discord.ext import commands
from bs4 import BeautifulSoup
import requests
import random

whiskey_url = 'http://whiskeycrow.com/Graal/heads/'
mafukie_url = 'https://graalserver.com/assets/images/'
ext = 'gif'

def list_dir(url, ext=''):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    return [node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]

class Ghead:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ghead(self, head):

        files = list_dir(whiskey_url, ext)
        if head + ".gif" in files:
            await self.bot.say("http://whiskeycrow.com/Graal/heads/" + head + ".gif")
        else:
            await self.bot.say(head + " not found, noob")

    @commands.command()
    async def grand(self):

        files = list_dir(whiskey_url, ext)
        await self.bot.say("http://whiskeycrow.com/Graal/heads/" + random.choice(files))


    @commands.command()
    async def gimg(self):

        r = requests.get(mafukie_url)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        link = soup.find('a')
        await self.bot.say(mafukie_url + link.get('href')

def setup(bot):
    bot.add_cog(Ghead(bot))
