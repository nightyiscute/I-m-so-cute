import random
import json
import discord
from discord.ext import commands

with open('data.json',mode='r',encoding='utf8')as jfile:
    jdata=json.load(jfile)


class hentai(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    option=discord.Option
    nhentai=discord.SlashCommandGroup("nhentai","( ͡° ͜ʖ ͡°)")


    @nhentai.command()
    async def random_num(self,ctx):
        random_int=random.randint(1,999999)
        await ctx.respond(f'https://nhentai.net/g/{random_int}/')

    @nhentai.command()
    async def godnum(self,ctx,num:int,page:option(int,"page",required = False)):
        if page==None:
            page=""
        await ctx.respond(f'https://nhentai.net/g/{num}/{page}')
    
    @nhentai.command()
    async def tag(self,ctx,tag:str):
        await ctx.respond(f"https://nhentai.net/tag/{tag}/")
    
    @nhentai.command()
    async def random_tag(self,ctx):
        ran=random.randint(0,148)
        await ctx.respond(f"https://nhentai.net/tag/{jdata[ran][0]}/")

    禁漫=discord.SlashCommandGroup("禁漫","就是禁漫")

    @禁漫.command()
    async def godnum(self,ctx,num:int,page:option(int,"page",required=False)):
        if page==None:
            page=""
        await ctx.respond(f'https://18comic.vip/photo/{num}/{page}')
    

def setup(bot):
    bot.add_cog(hentai(bot))