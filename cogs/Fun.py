import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import requests
import json



# async def TTTWinner(liste,stri):
#     if liste[0][0] == stri and liste[0][1] == stri and liste[0][2] == stri:
#         return True
#     if liste[1][0] == stri and liste[1][1] == stri and liste[1][2] == stri:
#         return True
#     if liste[2][0] == stri and liste[2][1] == stri and liste[2][2] == stri:
#         return True
#     if liste[0][0] == stri and liste[1][0] == stri and liste[2][0] == stri:
#         return True
#     if liste[0][1] == stri and liste[1][1] == stri and liste[2][1] == stri:
#         return True
#     if liste[0][2] == stri and liste[1][2] == stri and liste[2][2] == stri:
#         return True
#     if liste[0][0] == stri and liste[1][1] == stri and liste[2][2] == stri:
#         return True
#     if liste[2][0] == stri and liste[1][1] == stri and liste[0][2] == stri:
#         return True
#     return False
#
# async def CellTaken(liste,x,y):
#     if liste[x][y]==0:
#         return False
#     return True
#
# async def ConvertIntoTuple(stri):
#     if stri[0] == 'a' or stri[0] == 'A':
#         x=0
#     if stri[0] == 'b' or stri[0] == 'B':
#         x=1
#     if stri[0] == 'c' or stri[0] == 'C':
#         x=2
#     if stri[1] == '1':
#         y=0
#     if stri[1] == '2':
#         y=1
#     if stri[1] == '3':
#         y=2
#     return (x,y)
#
# async def PlaceonBoard(stri,liste,letter):
#         coords = await ConvertIntoTuple(stri)
#         if await CellTaken(liste,coords[0],coords[1]) == False:
#             liste[coords[0]][coords[1]] = letter
#             return True
#         else:
#             return False
#
# async def CheckTurn(turn):
#     return (turn[0]%2)
#
# async def IncreaseTurn(turn):
#     turn[0]+=1
#
# async def ZeroTurn(turn):
#     turn[0]=0

class Fun:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='devox', hidden = True)
    async def devox(self, ctx):
            """Signature command for the person who created the bot (me)."""
            member = discord.utils.find(lambda m: m.id == 250865328194715658, ctx.channel.guild.members)
            await ctx.send("{} The great man who created this bot some people say he has too much power, but the truth is he doesnt have enough".format(member.mention))

    # @commands.command(name='add')
    # async def add(self, ctx, left : int, right : int):
    #     """Adds two numbers together."""
    #     await ctx.send(left + right)

    @commands.command(name='roll')
    async def roll(self, ctx, dice : str):
        """Rolls a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return

        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @commands.command(name='8ball')
    async def ball(self, ctx):
        """8Ball Question/Answer."""
        answerpool = ["Of course it is",
                            "No, just No.",
                            "Without a doubt",
                            "Yes definitely",
                            "You may rely on it",
                            "i can predict that, yes",
                            "Most likely",
                            "Yep",
                            "My agents say yes",
                            "My agents say no",
                            "i am too lazy right now go away",
                            "Perhapsi yes perhapsi no",
                            "maybe :3",
                            "Don't count on it",
                            "My reply is no",
                            "My sources say no",
                            "Very doubtful",
                            "YESSSS"]
        await ctx.send(random.choice(answerpool))

    @commands.command(name='choose')
    async def choose(self, ctx, *choices : str):
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    # @commands.command(name='say')
    # async def say(self, ctx):
    #     """Makes the bot says whatever you want."""
    #     if (not ctx.message.author.guild_permissions.kick_members):
    #         return
    #     args = ctx.message.content.split(" ")[1:]
    #     await ctx.message.delete()
    #     await ctx.channel.send(" ".join(args))


    # @commands.command(name="tictactoe")
    # async def tictactoe(self,ctx,other : discord.Member=None):
    #     """play tic tac toe"""
    #     if other is None:
    #         await ctx.send("Uh, you entered no Member! Use a mention!")
    #         return
    #     authorr=ctx.message.author
    #     board=[[0,0,0],[0,0,0],[0,0,0]]
    #     letter1='O'
    #     letter2='X'
    #     turns=[0]
    #     @ctx.bot.event
    #     async def on_message(message):
    #         def check(message):
    #             if message.author.id != other.id and message.author.id != authorr.id:
    #                 return
    #             if message.author.id == other.id:
    #                 return ((message.content == 'confirm' or message.content == 'Confirm')and message.channel == ctx.message.channel)
    #         # msg = await ctx.bot.wait_for('message1', check=check, timeout=60)
    #         if check(message) == True:
    #             await ctx.send('ITS TIME TO D-D-D-D--D-D-DUEEEEEL! {} AGAINST {}'.format(ctx.author.mention, other.mention))
    #
    #         if (await TTTWinner(board,letter1) and turns[0]!=0):
    #             await ctx.send("The winner is {}".format(ctx.message.author.mention))
    #             await ZeroTurn(turns)
    #         if (await TTTWinner(board,letter2) and turns[0]!=0):
    #             await ctx.send("The winner is {}".format(other.mention))
    #             await ZeroTurn(turns)
    #         if (((await TTTWinner(board,letter1))==False) and ((await TTTWinner(board,letter2)) == False)) and (message.content != 'confirm' and message.content != 'Confirm'):
    #             print(message.content)
    #             if authorr.id == message.author.id and (await CheckTurn(turns))==0:
    #                 print(turns[0])
    #                 await PlaceonBoard(message.content,board,letter1)
    #                 await ctx.send("{} placed an O on {}".format(author.mention,message.content))
    #                 await IncreaseTurn(turns)
    #             if other.id == message.author.id and (await CheckTurn(turns))==1:
    #                 print(turns[0])
    #                 await PlaceonBoard(message.content,board,letter2)
    #                 await ctx.send("{} placed an O on {}".format(other.mention,message.content))
    #                 await IncreaseTurn(turns)
    #
    #


    @commands.command(name='getdoge')
    async def getdoge(self,ctx):
        """ Summon a member of the doge army."""
        async with self.bot.pool.acquire() as conn:
                async with conn.cursor() as cur:
                        await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                        isregistered = await cur.fetchone()
                        if isregistered: 
                                return
                        else:       
                            picurl = requests.get("https://dog.ceo/api/breed/shiba/images/random")
                            picurl = json.loads(picurl.content)
                            meme=discord.Embed()
                            meme.set_image(url=picurl['message'])
                            await ctx.send('Such wow', embed= meme)

    @commands.command(name = 'botlink')
    async def botlink(self, ctx):
        """Gives you a link to invite the bot"""
        async with self.bot.pool.acquire() as conn:
                async with conn.cursor() as cur:
                        await cur.execute('SELECT * FROM BLChannels WHERE "id"=%s;', (ctx.message.channel.id,))
                        isregistered = await cur.fetchone()
                        if isregistered: 
                                return
                        else:       
                            embed = discord.Embed(title="Mafu, the multi use bot", colour=discord.Colour(0x6c56b0),url="https://discordapp.com/oauth2/authorize?client_id=432292171371118592&scope=bot") 
                            await ctx.send(embed=embed)

    @commands.command(name= 'buyticket')
    async def buyticket(self,ctx):
        "ticket to the league of legends tournament"
        async with self.bot.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute('SELECT * FROM Tournament WHERE "id"=%s', (ctx.message.author.id,))
                    isregistered = await cur.fetchone()
                    if isregistered: return
                    else:
                        await cur.execute('SELECT COUNT(*) FROM Tournament')
                        count = await cur.fetchone()
                        await cur.execute('INSERT INTO Tournament ("id", "ticketid") VALUES (%s, %s)', (ctx.message.author.id, count))
                        await ctx.send("You have been registered, your ticket number is {}".format(count))

    @commands.command(name='ticketstatus')
    async def ticketstatus(self,ctx, other:discord.Member=None):
        "ticket of the league of legends tournament"
        async with self.bot.pool.acquire() as conn:
                async with conn.cursor() as cur:
                    if (other == None):
                        other = ctx.message.author
                    await cur.execute('SELECT * FROM Tournament WHERE "id"=%s', (ctx.message.author.id,))
                    isregistered = await cur.fetchone()
                    if isregistered == False: return
                    else:
                        await cur.execute('SELECT ticketid FROM Tournament WHERE "id"=%s', (ctx.message.author.id,))
                        ticketid = await cur.fetchone();
                        embed = discord.Embed(colour=discord.Colour(0xff0000), description=(
                            f"```asciidoc\n[{str(other)}]\n```Ticketnumber : {ticketid[0]}\n <a:mafucoin:477237855786106891><a:mafucoin:477237855786106891><a:mafucoin:477237855786106891><a:mafucoin:477237855786106891>\nOpponent :\n"))
                        embed.set_thumbnail(url=other.avatar_url)
                        embed.set_author(name=(f"{str(other)}'s ticket"), icon_url="https://cdn.discordapp.com/attachments/432384140856262657/432492967572537344/mafuicon.png")
                        await ctx.send(embed=embed)

    # @commands.command(name='getcat')
    # async def getcat(self,ctx):
    #     """ Give you a random pic of a cat."""
    #     picurl = requests.get("http://thecatapi.com/?id=clk")
    #     picurl = json.loads(picurl.content)
    #     meme=discord.Embed()
    #     meme.set_image(url=picurl['src'])
    #     await ctx.send(embed= meme)
    

def setup(bot): 
    bot.add_cog(Fun(bot))