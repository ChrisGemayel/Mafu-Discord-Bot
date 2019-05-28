import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot
import random
import json
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import os
from io import BytesIO
import sys, traceback
import aiopg
import aiohttp
import secrets, time
from PIL import Image, ImageDraw, ImageFont

with open('config.json') as data_file:    
    config = json.load(data_file)


bot = commands.Bot(command_prefix=config['prefix'], description=config['description'])


cogs_dir = "cogs"
if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    if not hasattr(bot, 'appinfo'):
        bot.appinfo = await bot.application_info()

    print('Mafu bot playing on ',len(bot.guilds),'servers hosting ', len(set(bot.get_all_members())), "members")
    gameplayed = discord.Game(name='playing with Wolf-not senpai')
    await bot.change_presence(activity = gameplayed)

    bot.session = aiohttp.ClientSession(loop=bot.loop)

bot.last_time = time.time()
@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if secrets.randbelow(8) == 1 and time.time() > bot.last_time + 60:
        money = random.randint(1,300)
        pic=discord.Embed()
        pic.set_image(url="https://cdn.discordapp.com/attachments/440867661136527360/477433070300037120/drop_background.gif")
        await message.channel.send("Mafu just dropped {} <a:mafucoin:477237855786106891> on the ground".format(money),embed=pic, delete_after=60)
        bot.last_time = time.time()
    await bot.process_commands(message)

async def download_image(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            return BytesIO(await r.read())

@bot.event
async def on_member_join(member):
    with Image.open('Z:\Bot\Mafu\mafusig.png') as image:
        with Image.open(await download_image(url=member.avatar_url_as(format="png"))) as img:
            img.thumbnail((300,300))
            image.paste(img,(700,0))
            with Image.open('Z:\Bot\Mafu\mask.png') as mask:
                image.paste(mask,(0,0), mask=mask)
                font_type = ImageFont.truetype('Montserrat-Bold.otf',70)
                font_type2 = ImageFont.truetype('Montserrat-Bold.otf',100)
                if (len(member.name)>=8 and len(member.name)<10):
                    font_type2 = ImageFont.truetype('Montserrat-Bold.otf',80)
                if (len(member.name)>=10):
                    font_type2 = ImageFont.truetype('Montserrat-Bold.otf',60)
                draw = ImageDraw.Draw(image)
                welcomemsg = "Welcome ~"
                welcomemsg2 = "\n  " + member.name
                draw.text(xy=(100,80), text=welcomemsg, fill=(0,159,219), font=font_type)
                draw.text(xy=(100,60), text=welcomemsg2, fill=(255,29,104), font=font_type2)

                img2 = BytesIO()
                image.save(img2, format="png")
                img2.seek(0)

                f = discord.File(img2, filename="image.png")
                pic = discord.Embed()
                pic.set_image(url = "attachment://image.png")
                for channels in member.guild.channels:
                    if channels.name == "chat":
                        channel=channels
                        break
                    if channels.name == "chit-chat":
                        channel=channels
                        break
                    if channels.name == "lounge":
                        channel=channels
                        break
                    if channels.name == "general":
                        channel=channels
                        break

                await channel.send("Hi there {}! Thanks for stopping by, now you're one of us\n Don't forget to read the rules, they are important :blue_heart:".format(member.mention),file=f, embed=pic)




async def create_pool():
    connstring = 'dbname=postgres user=postgres password=password host=127.0.0.1'
    pool = await aiopg.create_pool(connstring)
    return pool

async def start_bot():
    pool = await create_pool()
    bot.close()
    bot.pool = pool
    # bot.loop.create_task(mybgtask())
    await bot.start(config['token'])


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())


