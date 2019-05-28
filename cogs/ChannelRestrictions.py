import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import aiopg
import aiohttp
from discord.ext.commands.cooldowns import BucketType
import random


class ChannelRestrictions:
        def __init__(self, bot):
                self.bot = bot

        @commands.command(name='blchannel')
        async def blchannel(self, ctx):
                "Black list a channel"
                if (not ctx.message.author.guild_permissions.administrator):
                        await ctx.send("You need to be an administrator.")
                        return
                try:
                        args= ctx.message.content.split(" ")[1:]
                        args= " ".join(args)
                        channel = discord.utils.find(lambda x: x.name == args, ctx.message.guild.channels)
                except:
                        await ctx.send("That channel does not exist")

                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (channel.id,))
                                isregistered = await cur.fetchone()
                                if not isregistered:            
                                        try:
                                                await cur.execute('INSERT INTO  BLChannels ("id", "guildid") VALUES (%s, %s);', (channel.id, ctx.message.guild.id))
                                                await ctx.send("Successfully blacklisted channel.")  
                                        except:
                                                await ctx.send("An error occured when registering this channel.")
                                else:
                                        await ctx.send("This channel is already registered.")


        @commands.command(name='delblchannel')
        async def delblchannel(self, ctx):
                "remove channel from blacklist"
                if (not ctx.message.author.guild_permissions.administrator):
                        await ctx.send("You need to be an administrator.")
                        return
                try:
                        args= ctx.message.content.split(" ")[1:]
                        args= " ".join(args)
                        channel = discord.utils.find(lambda x: x.name == args, ctx.message.guild.channels)
                except:
                        await ctx.send("That channel does not exist")
                        
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered:            
                                        try:
                                                await cur.execute('DELETE FROM BLChannels WHERE "id"=%s;', (channel.id,))
                                                await ctx.send("Successfully removed channel from blacklist")  
                                        except:
                                                await ctx.send("An error occured when deleting this channel.")
                                else:
                                        await ctx.send("This channel is not blacklisted.")

                        


def setup(bot): 
        bot.add_cog(ChannelRestrictions(bot))
