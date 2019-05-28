import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import aiopg
import aiohttp
from discord.ext.commands.cooldowns import BucketType
import random


class Logs:
    def __init__(self, bot):
        self.bot = bot






def setup(bot):
    bot.add_cog(Logs(bot))
