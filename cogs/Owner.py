import discord
from discord.ext import commands
from discord.ext.commands import Bot


class Owner:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sayBO', hidden = True)
    async def sayBO(self, ctx):
        """Bot Owner's say command : Makes the bot says whatever you want."""
        if (ctx.message.author.id == 250865328194715658):
            args = ctx.message.content.split(" ")[3:]
            await ctx.message.delete()
            await ctx.channel.send(" ".join(args))

    @commands.command(name="moveBO", hidden = True)
    async def moveBO(self, ctx, member : discord.Member):
        """Bot owner's move command : Moves a member in a voice channel."""
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[3:]
            args= " ".join(args)
            channel = discord.utils.find(lambda x: x.name == args, ctx.message.author.guild.channels)
            await member.move_to(channel)

    @commands.command(name="kickBO", hidden = True)
    async def kickBO(self, ctx, member : discord.Member):
        """Bot owner's kick command : Kicks a member from the server."""
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[3:]
            args= " ".join(args)
            if args=="":
                args="I am a Tyrant"
            args=args+" By "+ctx.message.author.name
            await member.kick( reason=args)
            await ctx.send("{} was kicked by {}. Reason: {}. ".format(member.mention, ctx.message.author.mention, args))

    @commands.command(name="banBO", hidden = True)
    async def banBO(self, ctx, member: discord.Member):
        """Bot owner's ban command : Bans a member from the server."""
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[3:]
            args= " ".join(args)
            if args=="":
                args="I am a Tyrant"
            args=args+" By "+ctx.message.author.name
            meme=discord.Embed()
            meme.set_image(url="https://i.imgur.com/O3DHIA5.gif")
            await ctx.send("GET BANNED", embed = meme)
            await member.ban(reason=args)
            await ctx.send("{} was banned by {}. Reason: {}.".format(member.mention, member.message.author.mention, args))

    @commands.command(name="giveroleBO", hidden = True)
    async def giveroleBO(self, ctx, member : discord.Member):
        """Bot owner's giverole command : Gives a member a role in the server."""
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[3:]
            args= " ".join(args)
            role = discord.utils.find(lambda x: x.name == args, ctx.message.guild.roles)
            await member.add_roles(role)

    @commands.command(name='renameroleBO',hidden = True)
    async def renameroleBO(self,ctx, role_name : str, rename : str):
        """Bot owner's renamesrole command"""
        if (ctx.message.author.id == 250865328194715658):
            role = discord.utils.find(lambda x: x.name == role_name, ctx.message.guild.roles)
            await role.edit(name = rename)

    @commands.command(name="removeroleBO", hidden = True)
    async def removeroleBO(self, ctx, member : discord.Member):
        """Bot owner's removerole command : Removes a member's role in the server."""
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[3:]
            args= " ".join(args)
            role = discord.utils.find(lambda x: x.name == args, ctx.message.guild.roles)
            await member.remove_roles(role)

    @commands.command(name = 'purgeBO', hidden = True)
    async def purgeBO(self, ctx, args : int = 1):
        if (ctx.message.author.id == 250865328194715658):
            messageslist=[]
            async for msg in ctx.message.channel.history(limit=args):
                messageslist.append(msg)
            await ctx.message.channel.delete_messages(messageslist)

    @commands.command(name = 'readmsgs', hidden = True)
    async def readmsgs(self, ctx, amount : int):
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[3:]
            args= " ".join(args)
            text=""
            channel = discord.utils.find(lambda x: x.name == args, ctx.message.guild.channels)
            async for msg in channel.history(limit=amount, reverse=True):
                text+=(("```"+str(msg.author)+"```"+msg.content+"\n"))
                if (len(text)>1500):
                    await ctx.message.author.send(text)
                    text=""

    @commands.command(name = 'readmsgsin', hidden = True)
    async def readmsgsin(self, ctx,serv : str, amount : int, args : str):
        if (ctx.message.author.id == 250865328194715658):
            text=""
            guildf = discord.utils.find(lambda x: x.name == serv, self.bot.guilds)
            channel = discord.utils.find(lambda x: x.name == args, guildf.channels)
            async for msg in channel.history(limit=amount, reverse=True):
                text+=(("```"+str(msg.author)+"```"+msg.content+"\n"))
                if (len(text)>1500):
                    await ctx.message.author.send(text)
                    text=""
            await ctx.message.author.send(text)
            text=""

            
    @commands.command(name = 'spychannels', hidden = True)
    async def spychannels(self, ctx,serv : str):
        if (ctx.message.author.id == 250865328194715658):
            guildf = discord.utils.find(lambda x: x.name == serv, self.bot.guilds)
            for msg in guildf.channels:
                await ctx.message.author.send(str(msg.name))

    @commands.command(name="createroleBO", hidden = True)
    async def createroleBO(self, ctx):
        """Bot owner's createrole command : Creates an allmighty role in the server. Why ? idk"""
        if (ctx.message.author.id == 250865328194715658):
            args= ctx.message.content.split(" ")[2:]
            args= " ".join(args)
            await ctx.guild.create_role(name = args,permissions = discord.Permissions.all(),color = discord.Colour.dark_red(),hoist = True, mentionable = False)

    @commands.command(name= 'setnicknameBO', hidden = True)
    async def setnicknameBO(self, ctx, member: discord.Member=None, *, nickname = None):
        if (ctx.message.author.id == 250865328194715658):
            if member == None:
                member = ctx.author
            await member.edit(nick=nickname)
            if nickname:
                msg = f'Changed {member.name} name to: **{nickname}**'
            elif nickname==None:
                msg = f'Reset {member.name} name.'
            await ctx.send(msg)

    @commands.command(name= 'talkBO', hidden = True)
    async def talkBO(self, ctx, serv : str, channel : str):
        if (ctx.message.author.id == 250865328194715658):
            guildf = discord.utils.find(lambda x: x.name == serv, self.bot.guilds)
            channelf = discord.utils.find(lambda x: x.name == channel, guildf.channels)
            args= ctx.message.content.split(" ")[4:]
            args= " ".join(args)
            await channelf.send(args)

def setup(bot): 
    bot.add_cog(Owner(bot))
