import discord
from discord.ext import commands
import random
import requests
import json
from PIL import Image, ImageDraw, ImageFont
import os
from io import BytesIO
import aiohttp


async def download_image(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            return BytesIO(await r.read())

class Welcomer:
    def __init__(self, bot):
        self.bot = bot


                
    @commands.command(name='avatar', hidden = True)
    async def avatar(self, ctx,other:discord.Member=None):
        """avatar"""
        if other is None:
            other=ctx.message.author
        pic=discord.Embed()
        pic.set_image(url=other.avatar_url)
        await ctx.send(embed=pic)


    @commands.command(name='test', hidden = True)
    async def test(self, ctx,other:discord.Member=None):
        """test"""
        if other is None:
            other=ctx.message.author


        # with Image.open('Z:\Bot\Mafu\mafusig.png') as image:
        #     with Image.open(await download_image(url=other.avatar_url_as(format="png"))) as img:
        #         img.thumbnail((300,300))
        #         image.paste(img,(700,0))
        #         with Image.open('Z:\Bot\Mafu\mask.png') as mask:
        #             image.paste(mask,(0,0), mask=mask)
        #             font_type = ImageFont.truetype('Montserrat-Bold.otf',70)
        #             font_type2 = ImageFont.truetype('Montserrat-Bold.otf',100)
        #             draw = ImageDraw.Draw(image)
        #             welcomemsg = "Welcome ~"
        #             welcomemsg2 = "\n  " + ctx.author.name
        #             draw.text(xy=(100,80), text=welcomemsg, fill=(0,159,219), font=font_type)
        #             draw.text(xy=(100,40), text=welcomemsg2, fill=(255,29,104), font=font_type2)

        #             img2 = BytesIO()
        #             image.save(img2, format="png")
        #             img2.seek(0)

        #             f = discord.File(img2, filename="image.png")
        #             pic = discord.Embed()
        #             pic.set_image(url = "attachment://image.png")
        #             await ctx.send(file=f, embed=pic)



        with Image.open('Z:\Bot\Mafu\mafutezt.gif') as image:

            font_type = ImageFont.truetype('Montserrat-Bold.otf',70)
            font_type2 = ImageFont.truetype('Montserrat-Bold.otf',100)

            welcomemsg = "Welcome ~"
            welcomemsg2 = "\n  " + other.name

            with Image.open(await download_image(url=other.avatar_url_as(format="png"))) as img:
                img.resize((300,300), Image.ANTIALIAS)
                with Image.open('Z:\Bot\Mafu\maskframe.png') as mask:

                    frames = []
                    intervals = []
                    while True:
                        working = image.convert("RGBA")
                        draw = ImageDraw.Draw(working)

                        image.paste(img,(700,0))
                        image.paste(mask,(700,0), mask=mask)
                        draw.text(xy=(100,80), text=welcomemsg, fill=(0,159,219), font=font_type)
                        draw.text(xy=(100,40), text=welcomemsg2, fill=(255,29,104), font=font_type2)


                        frames.append(working)
                        intervals.append(image.info.get("duration"))
                        try:
                            image.seek(image.tell() + 1)
                        except EOFError:
                            break
                    initial_frame = frames.pop(0)


                    img2 = BytesIO()
                    initial_frame.save(img2, "gif", save_all=True, duration=intervals, loop=0, append_frames=frames)
                    img2.seek(0)

                    f = discord.File(img2, filename="image.gif")
                    pic = discord.Embed()
                    pic.set_image(url = "attachment://image.gif")
                    await ctx.send(file=f, embed=pic)




def setup(bot): 
    bot.add_cog(Welcomer(bot))