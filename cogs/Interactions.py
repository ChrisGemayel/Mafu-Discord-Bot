import discord
from discord.ext import commands
import random


class Interactions:
        def __init__(self, bot):
                self.bot = bot


        @commands.command(name='pat')
        async def pat(self, ctx):
                """Pat command : Pat someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432499837104160768/mafupat2.gif")
                                        await ctx.send("{} has been pated by {} ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='heartbroken')
        async def heartbroken(self, ctx):
                """Heartbroken command : Someone broke your heart"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432499829235777546/mafuheartbroke.gif")
                                        await ctx.send("{} broke {}'s heart ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='poke')
        async def poke(self, ctx):
                """poke command : you poke someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432516130842869760/mafupoke.gif   ")
                                        await ctx.send("{} got poked by {} ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='love')
        async def love(self, ctx):
                """love command : you love someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432493033477636105/mafulove.gif")
                                        await ctx.send("{} is loved by {} ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='patpat')
        async def patpat(self, ctx):
                """patpat command : you patpat someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432493037755564032/mafupat.gif")
                                        await ctx.send("{} is pated vigorously by {} ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='hug')
        async def hug(self, ctx):
                """hug command : you hug someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        liste=["https://cdn.discordapp.com/attachments/432384604066938880/432493043879510027/mafuhug.gif","https://cdn.discordapp.com/attachments/432384604066938880/432499832322654219/mafuhug3.gif","https://cdn.discordapp.com/attachments/432384604066938880/432499834675658762/mafuhug4.gif","https://cdn.discordapp.com/attachments/432384604066938880/432493045502443521/mafuhug2.gif"]
                                        meme.set_image(url=random.choice(liste))
                                        await ctx.send("{} is hugged by {} ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='sleep')
        async def sleep(self, ctx):
                """sleep command : you sleep"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432499827448741888/mafusleep.gif")
                                        await ctx.send("{} is sleepy ".format(ctx.author.mention), embed = meme)

        @commands.command(name='cry')
        async def cry(self, ctx):
                """cry command : someone made you cry """
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432499831517216768/mafucry.gif   ")
                                        await ctx.send("{} made {} cry ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='nuzzle')
        async def nuzzle(self, ctx):
                """nuzzle command : you nuzzle someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        liste=["https://cdn.discordapp.com/attachments/432384604066938880/432516439275208706/mafunuzzle2.gif","https://cdn.discordapp.com/attachments/432384604066938880/432499835191689246/mafunuzzle.gif"]
                                        meme.set_image(url=random.choice(liste))
                                        await ctx.send("{} is nuzzled by {} ".format(ctx.message.mentions[0].mention, ctx.author.mention), embed = meme)

        @commands.command(name='bite')
        async def bite(self, ctx):
                """bite command : you bite someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432516164900487188/mafubite2.gif")
                                        await ctx.send("{} bit {} ".format(ctx.author.mention, ctx.message.mentions[0].mention), embed = meme)

        @commands.command(name='kiss')
        async def kiss(self, ctx):
                """kiss command : you kiss someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        liste=["https://cdn.discordapp.com/attachments/432384604066938880/432515089401249805/mafukiss4.gif","https://cdn.discordapp.com/attachments/432384604066938880/432514224879829002/mafukiss3.gif"]
                                        meme.set_image(url=random.choice(liste))
                                        await ctx.send("{} kissed {} ".format(ctx.author.mention, ctx.message.mentions[0].mention), embed = meme)

        @commands.command(name='fight')
        async def fight(self, ctx):
                """fight command : you fight with someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432514520754290688/mafubite.gif")
                                        await ctx.send("{} fights with {} ".format(ctx.author.mention, ctx.message.mentions[0].mention), embed = meme)

        @commands.command(name='angery')
        async def angery(self, ctx):
                """angery command : you are angery at someone"""
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                else:       
                                        meme=discord.Embed()
                                        meme.set_image(url="https://cdn.discordapp.com/attachments/432384604066938880/432501664902021140/mafuangery.gif")
                                        await ctx.send("{} is angery at {} ".format(ctx.author.mention, ctx.message.mentions[0].mention), embed = meme)



def setup(bot): 
        bot.add_cog(Interactions(bot))
