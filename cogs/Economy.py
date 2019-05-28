import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import aiopg
import aiohttp
from discord.ext.commands.cooldowns import BucketType
import random



class Economy:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ecohelp")
    async def ecohelp(self,ctx):
                async with self.bot.pool.acquire() as conn:
                        async with conn.cursor() as cur:
                                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                                isregistered = await cur.fetchone()
                                if isregistered: 
                                        return
                                await ctx.send("Commands for economy are :\n```asciidoc\n= t~daily                       = \n= t~beg                         =\n= t~profile                     = \n= t~flip amount                 =\n= t~leaderboard                 =\n= t~tp                          =\n= t~tpleaderboard               =\n= t~bb or t~bloodmoney          =\n= t~claim                       = \n= t~steal                       =\n= t~give                        =\n```")


    @commands.command(name='economy', aliases=["money", "balance","bal"])
    async def economy(self, ctx, other:discord.Member=None):
        """Shows your current balance."""
        if (other == None):
            other = ctx.message.author
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregistered = await cur.fetchone()
                if isregistered: 
                        return
                try:
                    await cur.execute('SELECT * from money WHERE "id"=%s;', (other.id,))
                except:
                    await ctx.send("An error occured when fetching your balance data.")
                ret = []
                async for row in cur:
                    ret.append(row)
        if ret==[]:
            await ctx.send("You are not registered yet.")
        else:
            data = ret[0]
            await ctx.send(f"{other.mention} currently has ** <a:mafucoin:477237855786106891> {data[1]}**!")

    @commands.command(name='register')
    async def register(self, ctx):
        """Register yourself"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                await cur.execute('SELECT * FROM money WHERE "id"=%s;', (ctx.message.author.id,))
                isregistered = await cur.fetchone()
                await cur.execute('SELECT * FROM bloodmoney WHERE "id"=%s;', (ctx.message.author.id,))
                isregisteredblood = await cur.fetchone()
                if not isregistered:            
                    try:
                        await cur.execute('INSERT INTO  money ("id", "money") VALUES (%s, %s);', (ctx.message.author.id, 1000)) 
                        await ctx.send("Successfully registered you.")  
                    except:
                        await ctx.send("An error occured when registering you.")
                if not isregisteredblood:
                    try:
                        await cur.execute('INSERT INTO  bloodmoney ("id", "bloodmoney","thiefpower") VALUES (%s, %s,%s);', (ctx.message.author.id, 0,0))
                    except:
                        await ctx.send("An error occured when registering you.")
                else:
                    await ctx.send("You are already registered.")
                    await ctx.reset_cooldown(ctx)

    @commands.command(name='give')
    async def give(self, ctx, money: int, other:discord.Member=None):
        """Gift money"""

        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                if money<0:
                    await ctx.send("Don't scam!")
                    return
                if other is None:
                    await ctx.send("Uh, you entered no Member! Use a mention!")
                    return
                if other == ctx.message.author:
                    await ctx.send("No cheating!")
                    return
                try:
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;', (ctx.message.author.id,))
                    money1 = await cur.fetchone()
                    if money1[0]<money:
                        await ctx.send("You are too poor.")
                        return
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;', (other.id,))
                    money2 = await cur.fetchone()
                    if not money2:
                        await("The other person is not registered")
                    await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money1[0]-money, ctx.message.author.id))
                    await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]+money, other.id))
                    await ctx.send(f"Successfully gave **<a:mafucoin:477237855786106891>{money}** to {other.mention}.")
                except:
                    await ctx.send("Either you or the other person are not registered.")
                    await ctx.reset_cooldown(ctx)

    @commands.command(name='steal')
    @commands.cooldown(1,300,BucketType.user)  
    async def steal(self, ctx,other:discord.Member=None):
        """Steal Money from another member"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                if other is None:
                    await ctx.send("Uh, you entered no Member! Use a mention!")
                    return
                if other == ctx.message.author:
                    await ctx.send("No cheating!")
                    return
                try:
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;', (ctx.message.author.id,))
                    money1 = await cur.fetchone()
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;', (other.id,))
                    money2 = await cur.fetchone()
                    liste=["Heads","Tails"]
                    result = random.choice(liste)
                    await cur.execute('SELECT bloodmoney FROM bloodmoney WHERE "id"=%s;', (ctx.message.author.id,))
                    bloodmoney1 = await cur.fetchone()
                    if money1[0] < 100 and bloodmoney1[0]< 1000:
                        moneyarg = random.randint(0, 300)
                    else:
                        moneyarg = random.randint(0,1000)
                    if money2[0]<5000:
                        await ctx.send("Dont steal from the poor.")
                        return
                    if other.id == 214371620368678914:
                        if money1[0]<moneyarg:
                            moneyarg=money1[0]
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money1[0]-moneyarg, ctx.message.author.id))
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]+moneyarg, other.id))
                        await ctx.send(f"{ctx.author.mention} one does not simply steal from {str(other)}-sama he knocks you out and takes ** <a:mafucoin:477237855786106891> {moneyarg}**.")
                        return
                    if (result == "Heads"):
                        await cur.execute('UPDATE bloodmoney SET "bloodmoney"=%s WHERE "id"=%s', (bloodmoney1[0]+moneyarg, ctx.message.author.id))
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]-moneyarg, other.id))
                        await ctx.send(f"{ctx.author.mention} you stole  <a:mafucoin:477237855786106891> **{moneyarg}** from {str(other)}. Nice going thief")
                    else:
                        if bloodmoney1[0]<=moneyarg:
                            if money1[0]<moneyarg:
                                moneyarg=money1[0]
                            await ctx.send(f"{ctx.author.mention} you failed stealing from {str(other)} instead he/she takes  <a:mafucoin:477237855786106891>  {moneyarg} of your money.")
                            await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money1[0]-moneyarg, ctx.message.author.id))
                            await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]+moneyarg, other.id))
                            return
                        await cur.execute('UPDATE bloodmoney SET "bloodmoney"=%s WHERE "id"=%s', (0, ctx.message.author.id))
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]+bloodmoney1[0], other.id))
                        await ctx.send(f"{ctx.author.mention} you failed stealing from {str(other)} instead he/she beats you up and takes <a:mafucoin:477237855786106891> **{bloodmoney1[0]}**.")

                except:
                    await ctx.send("Either you or the other person are not registered.")
                    await ctx.reset_cooldown(ctx)

    @commands.command(name="claim")
    @commands.cooldown(1,3600,BucketType.user)
    async def claim(self, ctx):
        """ Fence the blood money you stole"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                    isregisteredc = await cur.fetchone()
                    if isregisteredc: 
                            return
                    await cur.execute('SELECT bloodmoney FROM bloodmoney WHERE "id"=%s;',(ctx.author.id,))
                    bloodmoney = await cur.fetchone()
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;',(ctx.author.id,))
                    money = await cur.fetchone()
                    await cur.execute('SELECT thiefpower FROM bloodmoney WHERE "id"=%s;',(ctx.author.id,))
                    thiefpower = await cur.fetchone()
                    await cur.execute('UPDATE bloodmoney SET "thiefpower"=%s WHERE "id"=%s;',(thiefpower[0]+bloodmoney[0],ctx.message.author.id))
                    await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s;', (money[0]+bloodmoney[0], ctx.message.author.id))
                    await cur.execute('UPDATE bloodmoney SET "bloodmoney"=%s WHERE "id"=%s;', (0, ctx.message.author.id))
                    await ctx.send(f"You fenced {bloodmoney[0]} <a:mafucoin:477237855786106891> blood money! Good job.")
                except:
                    await ctx.send("You are not registered.")
                    await ctx.reset_cooldown(ctx.command)

    @commands.command(name="gimme")
    async def gimme(self, ctx):
        """ Claims money droped by mafu"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                try:
                    await cur.execute('SELECT * FROM money WHERE "id"=%s;', (ctx.message.author.id,))
                    print(1)
                    # isregisteredc = await cur.fetchone()
                    print(2)
                    # if not isregisteredc:
                    #     try:
                    #         print(3)
                    #         await cur.execute('INSERT INTO  money ("id", "money") VALUES (%s, %s);',(ctx.message.author.id, 1000))
                    #         await ctx.send("Successfully registered you.")
                    #     except:
                    #         await ctx.send("An error occured when registering you.")
                    # if not isregisteredblood:
                    #     try:
                    #         print(4)
                    #         await cur.execute('INSERT INTO  bloodmoney ("id", "bloodmoney","thiefpower") VALUES (%s, %s,%s);',(ctx.message.author.id, 0, 0))
                    #     except:
                    #         await ctx.send("An error occured when registering you.")
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;',(ctx.author.id,))
                    money = await cur.fetchone()
                    dropmoney=0
                    print(5)
                    # await ctx.author.message.delete()
                    async for message in ctx.message.channel.history():
                        print(6)
                        if message.author.id == 419460455032029185 and message.embeds and message.content[:17]=="Mafu just dropped":
                            # emb = message.embeds[0]
                            # try:
                            #     title = emb.title
                            # except AttributeError:
                            #     return
                            dropmsg=message.content.split(" ")
                            dropmsg=int(dropmsg[3])
                            dropmoney+=dropmsg
                            await message.delete()

                    await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s;', (money[0]+dropmoney, ctx.message.author.id))
                    print(6.5)
                    pic=discord.Embed()
                    print(7)
                    pic.set_image(url="https://cdn.discordapp.com/attachments/440867661136527360/477432478571823105/ezgif.com-crop.gif")
                    await ctx.send("{} claimed {} <a:mafucoin:477237855786106891> mafu coins Good job!".format(ctx.author.mention,dropmoney), embed=pic, delete_after=20)
                except:
                    await ctx.send("You are not registered or there is nothing to claim", delete_after=20)



    @commands.command(name='thiefpower', aliases=["tp", "TP"])
    async def thiefpower(self, ctx, other:discord.Member=None):
        """Shows your current thief power."""
        if (other == None):
            other = ctx.message.author
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT * from bloodmoney WHERE "id"=%s;', (other.id,))
                except:
                    await ctx.send("An error occured when fetching your balance data.")
                ret = []
                async for row in cur:
                    ret.append(row)
        if ret==[]:
            await ctx.send("You are not registered yet.")
        else:
            data = ret[0]
            await ctx.send(f"{other.mention} currently has  **🔱 {data[2]}**  Thief Power aka TP!")

    @commands.command(name='bloodbal', aliases=["bb", "bbal"])
    async def bloodbal(self, ctx, other:discord.Member=None):
        """Shows the amount of bloodmoney you currently have."""
        if (other == None):
            other = ctx.message.author
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT * from bloodmoney WHERE "id"=%s;', (other.id,))
                except:
                    await ctx.send("An error occured when fetching your balance data.")
                ret = []
                async for row in cur:
                    ret.append(row)
        if ret==[]:
            await ctx.send("You are not registered yet.")
        else:
            data = ret[0]
            await ctx.send(f"{other.mention} currently has  ♦️** {data[1]}** bloodmoney!")

    def lookup(self, client, userid):
        return str(discord.utils.get(client.get_all_members(), id=userid))

    @commands.command(name="tpleaderboard")
    async def tpleaderboard(self, ctx):
        """Show leaderboard of the top thieves"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT * FROM bloodmoney ORDER BY "thiefpower" DESC LIMIT 10;')
                except:
                    await ctx.send("An error occured when fetching the data.")
                ret = []
                async for row in cur:
                    ret.append(row)
        if ret==[]:
            await ctx.send("Noone registered yet. Use `{ctx.prefix}register` to be the first one!")
        else:
            nl = "\n"
            result = f"**The best thieves are**:{nl}"
            for profile in ret:
                number = ret.index(profile)+1
                pstring = f"{number}. `{self.lookup(self.bot, profile[0])}` with  **🔱 {profile[2]}**{nl}"
                result += pstring
            await ctx.send(result)

    @commands.command(name="leaderboard")
    async def leaderboard(self, ctx):
        """Show leaderboard of the richest players"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT * FROM money ORDER BY "money" DESC LIMIT 10;')
                except:
                    await ctx.send("An error occured when fetching the data.")
                ret = []
                async for row in cur:
                    ret.append(row)
        if ret==[]:
            await ctx.send("Noone registered yet. Use `{ctx.prefix}register` to be the first one!")
        else:
            nl = "\n"
            result = f"**The people who have the most mafu coins are**:{nl}"
            for profile in ret:
                number = ret.index(profile)+1
                pstring = f"{number}. `{self.lookup(self.bot, profile[0])}` with  ** <a:mafucoin:477237855786106891> {profile[1]}**{nl}"
                result += pstring
            await ctx.send(result)

    @commands.command(name='profile', aliases=["pfl"])
    async def profile(self, ctx, other:discord.Member=None):
        """Shows your profile."""
        if (other == None):
            other = ctx.message.author
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT bloodmoney FROM bloodmoney WHERE "id"=%s;',(other.id,))
                    bloodmoney = await cur.fetchone()
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;',(other.id,))
                    money = await cur.fetchone()
                    await cur.execute('SELECT thiefpower FROM bloodmoney WHERE "id"=%s;',(other.id,))
                    thiefpower = await cur.fetchone()
                    await cur.execute('SELECT squad FROM bloodmoney WHERE "id"=%s;',(other.id,))
                    squad = await cur.fetchone()
                    embed = discord.Embed(colour=discord.Colour(0xff0000), description=(f"```asciidoc\n[{str(other)}]\n```Balance : {money[0]} <a:mafucoin:477237855786106891>\nThief Power : {thiefpower[0]} 🔱\nBounty/Bloodmoney : {bloodmoney[0]} ♦️\nSquad : {squad[0]}\n"))
                    embed.set_thumbnail(url=other.avatar_url)
                    embed.set_author(name=(f"{str(other)}'s profile"), icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")
                    await ctx.send(embed=embed)

                    if not squad:
                        squad="None"
                except:
                    await ctx.send("An error occured when fetching your balance data.")



    @commands.command(name="giveBO", hidden = True)
    async def giveBO(self, ctx, money: int, other:discord.Member=None):
        if (ctx.message.author.id == 250865328194715658):
            async with self.bot.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    try:
                        await cur.execute('SELECT money FROM money WHERE "id"=%s;', (other.id,))
                        money2 = await cur.fetchone()
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]+money, other.id))
                        await ctx.send(f"Successfully gave ** <a:mafucoin:477237855786106891> {money}** to {other.mention}.")
                    except:
                        await ctx.send("Either you or the other person are not registered.")

    @commands.command(name="removeBO", hidden = True)
    async def removeBO(self, ctx, money: int, other: int):
        if (ctx.message.author.id == 250865328194715658):
            async with self.bot.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    try:
                        await cur.execute('SELECT money FROM money WHERE "id"=%s;', (other,))
                        money2 = await cur.fetchone()
                        if (money>money2[0]):
                            await ctx.send("Poor guy, you cant remove more money than he actually has.")
                            return
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money2[0]-money, other))
                        await ctx.send(f"Successfully removed ** <a:mafucoin:477237855786106891> {money}** from {other}.")
                    except:
                        await ctx.send("the person is not registered.")

    @commands.command(name="daily")
    @commands.cooldown(1,86400,BucketType.user)
    async def daily(self, ctx):
        """Claim daily money"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT money FROM money WHERE "id"=%s;',(ctx.author.id,))
                    money = await cur.fetchone()
                    await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money[0]+200, ctx.message.author.id))
                    await ctx.send(f"You earned ** <a:mafucoin:477237855786106891> 200**.")
                except:
                    await ctx.send("You are not registered.")
                    await ctx.reset_cooldown(ctx)

    @commands.command(name="shop")
    async def shop(self, ctx):
        """Shop under construction"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
        embed = discord.Embed(title="**Welcome to the Shop choose wisely**", colour=discord.Colour(0x6808a0), description="\n:one: **- Melee Weapons   :crossed_swords: \n:two:  - Mage Weapons   :crystal_ball: \n:three:  - Food**  :ramen: ")

        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
        embed.set_author(name="Mystic Shop", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434284291518889984/Untitled.png")
        embed.set_footer(text=": Type in the number to browse whatever you want", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


        await ctx.send(embed=embed)

    @commands.command(name='beg')
    @commands.cooldown(1,60,BucketType.user)  
    async def beg(self,ctx):
        """Beg to make a bit of money"""
        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                try:
                    await cur.execute('SELECT money FROM money WHERE "id"=%s', (ctx.message.author.id,))
                    money = await cur.fetchone()
                    result = random.randint(0, 30)
                    if result ==0:
                        await ctx.send(f"{ctx.author.mention} shame on you for begging, no one showed kindness to you")
                        return
                    await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money[0]+result, ctx.message.author.id))
                    await ctx.send(f"{ctx.author.mention} shame on you for begging. you earned  ** <a:mafucoin:477237855786106891> {result}**.")
                except:
                    await ctx.send("You are not registered")



    @commands.command(name='flip')
    @commands.cooldown(1,10,BucketType.user)  
    async def flip(self,ctx, moneyarg : int=1 ):
        """Flip a coin while betting money on it"""

        async with self.bot.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                isregisteredc = await cur.fetchone()
                if isregisteredc: 
                        return
                if moneyarg<0:
                    await ctx.send("Don't scam!")
                    return
                # if (moneyarg > 5000):
                #     await ctx.send("You cant gamble more than 🔹5000 at once.")
                #     return
                try:
                    await cur.execute('SELECT money FROM money WHERE "id"=%s', (ctx.message.author.id,))
                    money = await cur.fetchone()
                    if money[0]<moneyarg:
                        await ctx.send("You are too poor.")
                        return
                    liste=["Heads","Tails"]
                    result = random.choice(liste)
                    if (result == "Heads"):
                        pic=discord.Embed()
                        pic.set_image(url="https://cdn.discordapp.com/attachments/432180512069517333/477242418752651264/smol_wiggle.gif")
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money[0]+moneyarg, ctx.message.author.id))
                        await ctx.send("{} You got **HEADS** , you earned  ** <a:mafucoin:477237855786106891> {}**.".format(ctx.author.mention, moneyarg), embed=pic)
                    else:
                        pic=discord.Embed()
                        pic.set_image(url="https://cdn.discordapp.com/attachments/432180512069517333/477245242760888330/smol_sad.gif")
                        await cur.execute('UPDATE money SET "money"=%s WHERE "id"=%s', (money[0]-moneyarg, ctx.message.author.id))
                        await ctx.send("{} You got **TAILS**, you lost ** <a:mafucoin:477237855786106891> {}**.".format(ctx.author.mention, moneyarg), embed=pic)
                except:
                    await ctx.send("You are not registered")
                    await ctx.reset_cooldown(ctx)


def setup(bot): 
    bot.add_cog(Economy(bot))





# embed = discord.Embed(colour=discord.Colour(0x606780), description="```WOODEN STICK ```A simple stick taken from a living tree.\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/430400227154067466/434317056725221386/wooden_sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#-------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0xffffff), description="```BRONZE SWORD ```This sword has seen a lot of action,\n but now its past its prime.\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/430400227154067466/434327875013967873/Bronze_sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#-------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0xff1b), description="```prolog\n'IRON SWORD' ```A bloodthirsty Gladius.\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/430400227154067466/434389402568097832/Iron_Sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0x8aa5ff), description="```prolog\n'STEEL KATANA' ```A fine blade only used by the ooga booga\n tribe. It can cut through bone with ease.\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/430400227154067466/434390310953549835/steel_katana.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0xff00b2), description="```prolog\n'SILVER RAPIER' ```A quick blade used by those with\n the finest tastes.\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/432642895762161674/434391111595982848/silver_rapier.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0xffeb00), description="```ml\nGOLDEN SWORD ```A Royal sword passed down \nthrough the generations.\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/432642895762161674/434392706966355968/golden_sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0x42ff), description="```asciidoc\n= PLATINUM SWORD = ```A holy sword capable of cutting\n the skies in half\n**PRICE : **")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/432642895762161674/434393751876796437/Platinum_Sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0xeeff), description="```asciidoc\n= DIAMOND SWORD = ```A Sword that took a century to forge \nthat can pierce anything.\n**PRICE : ** ")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/432642895762161674/434396786547884033/Diamond_Sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0x634aaf), description="```asciidoc\n= OBSIDIAN SWORD = ```A Cursed blade only the worthy \nhave ever survived using.\n**PRICE : ** ")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/432642895762161674/434397113489817600/Obsidian_Sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------

# embed = discord.Embed(colour=discord.Colour(0xff0000), description="```asciidoc\n[ DRAGON HEART SWORD ]```The Legendary Sword Saber Tooth \nwhere a Dragons Soul resides\n in the heart attached to its hilt,\n the sword speaks wisdom and \nguides its owner to the right path.\n**PRICE : ** ")

# embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/432642895762161674/434397133035143168/Dragon_Sword.png")
# embed.set_author(name="M.S. : Melee Weapons ⚔️", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/434283507360202754/85d4d47a5ebbb37c438e5f87d5ffc2ec.png")
# embed.set_footer(text=": type buy to buy this item.", icon_url="https://cdn.discordapp.com/attachments/430400227154067466/433532844170674188/icon.png")


# await bot.say(embed=embed)

#---------------------------------------------------------------------------------------------------------------