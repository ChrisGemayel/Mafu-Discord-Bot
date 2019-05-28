import discord
from discord.ext import commands


class Admin:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='move')
    async def move(self, ctx, member : discord.Member):
        """Moves a member in a voice channel."""
        if (not ctx.message.author.guild_permissions.kick_members):
            await ctx.send("Not enough permissions to move members.")
            return
        args= ctx.message.content.split(" ")[3:]
        args= " ".join(args)
        channel = discord.utils.find(lambda x: x.name == args, ctx.message.author.guild.channels)
        await member.move_to(channel)

    @commands.command(name='kick')
    async def kick(self, ctx, member : discord.Member):
        """Kicks a member from the server."""
        if ctx.message.author == member:
            await ctx.send("You can't kick yourself.")
            return
        elif (not ctx.message.author.guild_permissions.kick_members):
            await ctx.send("Not enough permissions to kick.")
            return
        elif (member.top_role > ctx.message.author.top_role):
            await ctx.send("You can't kick someone with a higher role.")
        args= ctx.message.content.split(" ")[3:]
        args= " ".join(args)
        if args=="":
            args="I am a Tyrant"
        args=args+" By "+ctx.message.author.name
        meme=discord.Embed()
        meme.set_image(url="https://cdn.discordapp.com/attachments/432180512069517333/478177761127563267/ezgif.com-gif-maker.gif")
        await ctx.send("Dont mess with mafu", embed = meme)
        await member.kick( reason=args)
        await ctx.send("{} was kicked by {}. Reason: {}. ".format(member.mention, ctx.message.author.mention, args))

    @commands.command(name='ban')
    async def ban(self, ctx, member: discord.Member):
        """Bans a member from the server."""
        if ctx.message.author == member:
            await ctx.send("You can't ban yourself.")
            return
        elif (not ctx.message.author.guild_permissions.administrator):
            await ctx.send("Not enough permissions to ban.")
            return
        elif (member.top_role > ctx.message.author.top_role):
            await ctx.send("You can't ban someone with a higher role.")
        args= ctx.message.content.split(" ")[3:]
        args= " ".join(args)
        if args=="":
            args="I am a Tyrant"
        args=args+" By "+ctx.message.author.name
        meme=discord.Embed()
        meme.set_image(url="https://cdn.discordapp.com/attachments/432180512069517333/478174296858951681/giphy_1.gif")
        await ctx.send("GET BANNED", embed = meme)
        await member.ban(reason=args)
        await ctx.send("{} was banned by {}. Reason: {}.".format(member.mention, member.message.author.mention, args))

    @commands.command(name='giverole')
    async def giverole(self, ctx, member : discord.Member):
        """Gives a member a role in the server."""
        if (not ctx.message.author.guild_permissions.administrator):
            await ctx.send("You need administrator rank to give out roles.")
            return
        args= ctx.message.content.split(" ")[3:]
        args= " ".join(args)
        role = discord.utils.find(lambda x: x.name == args, ctx.message.guild.roles)
        await member.add_roles(role)

    @commands.command(name='removerole')
    async def removerole(self, ctx, member : discord.Member):
        """Removes a member's role in the server."""
        if (not ctx.message.author.guild_permissions.administrator):
            await ctx.send("You need administrator rank to remove roles.")
            return
        args= ctx.message.content.split(" ")[3:]
        args= " ".join(args)
        role = discord.utils.find(lambda x: x.name == args, ctx.message.guild.roles)
        await member.remove_roles(role)

    @commands.command(name='createrole')
    async def createrole(self, ctx):
        """Creates an allmighty role in the server. Why ? idk"""
        if (not ctx.message.author.guild_permissions.administrator):
            await ctx.send("You need administrator rank to create roles.")
            return
        args= ctx.message.content.split(" ")[2:]
        args= " ".join(args)
        await ctx.guild.create_role(name = args,permissions = discord.Permissions.all(),color = discord.Colour.dark_red(),hoist = True, mentionable = False)

    @commands.command(name='renamerole')
    async def renamerole(self,ctx, role_name : str, rename : str):
        """Renames Roles"""
        if (not ctx.message.author.guild_permissions.manage_roles):
            await ctx.send("You need manage roles permission to rename roles.")
            return
        role = discord.utils.find(lambda x: x.name == role_name, ctx.message.guild.roles)
        rsn = "By {}".format(ctx.message.author.name)
        await role.edit(name = rename, reason = rsn)

    @commands.command(name='deleterole')
    async def deleterole(self, ctx, *, role_name : str):
        """Deletes a role"""
        if (not ctx.message.author.guild_permissions.administrator):
            await ctx.send("You do not have permissions to delete roles.")
            return
        role = discord.utils.find(lambda x: x.name == role_name, ctx.message.guild.roles)
        rsn = "By {}".format(ctx.message.author.name)
        await role.delete(reason=rsn)

    @commands.command(name= 'setnickname')
    async def setnickname(self, ctx, member: discord.Member=None, *, nickname = None):
        if (not ctx.message.author.guild_permissions.administrator):
            await ctx.send("You do not have permissions to change nicknames.")
            return
        if member == None:
            member = ctx.author
        await member.edit(nick=nickname)
        if nickname:
            msg = f'Changed {member.name} name to: **{nickname}**'
        elif nickname==None:
            msg = f'Reset {member.name} name.'
        await ctx.send(msg)

    @commands.command(name = 'purge')
    async def purge(self, ctx, args : int = 1):
        if (not ctx.message.author.guild_permissions.manage_messages):
            await ctx.send("You do not have permissions to manage messages.")
            return
        messageslist=[]
        async for msg in ctx.message.channel.history(limit=args):
            messageslist.append(msg)
        await ctx.message.channel.delete_messages(messageslist)

def setup(bot): 
    bot.add_cog(Admin(bot))
