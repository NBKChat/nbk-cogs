'''
================== Crypto Cog ==================
| Author  : Adam Valdez
| Source  : https://www.github.com/adamvaldez
| Website : https:www.planetcryptoid.tech
| Date    : 3/11/2018     
=================================================
'''

import discord
from discord.ext import commands
from urllib.request import urlopen
import json


class Crypto:
    """Planet Cryptoid's Crypto Price Cog (powered by coinmarketcap.com)"""

    def __init__(self, bot):
        self.bot = bot

    def get_jsonparsed_data(self, url):
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)

    @commands.command()
    async def btc(self):
        """What is Bitcoin's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/bitcoin"
        data = self.get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def eth(self):
        """What is Ethereum's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/ethereum"
        data = self.get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def xrp(self):
        """What is Ripple's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/ripple"
        data = self.get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def bch(self):
        """What is Bitcoin Cash's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/bitcoin-cash"
        response = self.urllib.request.urlopen(url)
        data = get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def ltc(self):
        """What is Litecoins's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/litecoin"
        response = self.urllib.request.urlopen(url)
        data = get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def neo(self):
        """What is NEO's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/neo"
        data = self.get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def xrm(self):
        """What is Monero's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/monero"
        data = self.get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")


    @commands.command()
    async def xlm(self):
        """What is Stellar's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/stellar"
        data = self.get_jsonparsed_data(url)
        await self.bot.say(data[0]['name'] + " is priced $" + data[0]['price_usd'] + " (" +
                            data[0]['percent_change_1h'] + "%)")

    @commands.command()
    async def top5(self):
        """Get top 5 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=5"
        data = self.get_jsonparsed_data(url)
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 5:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " (" +
                               data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1

    @commands.command()
    async def top10(self):
        """Get top 10 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        data = self.get_jsonparsed_data(url)
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 10:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " ("
                               + data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1


    @commands.command()
    async def top20(self):
        """Get top 20 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=20"
        data = self.get_jsonparsed_data(url)
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 20:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " ("
                               + data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1


def setup(bot):
    bot.add_cog(Crypto(bot))
