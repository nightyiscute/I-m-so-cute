import discord
import json
import random
from discord.ext import commands

with open('thing.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)
bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())
option=discord.Option

nhentai=bot.create_group("nhentai")
@nhentai.command()
async def random_num(ctx):
    random_int=random.randint(1,999999)
    await ctx.respond(f'https://nhentai.net/g/{random_int}/')
@nhentai.command()
async def godnum(ctx,num:int):
    await ctx.respond(f'https://nhentai.net/g/{num}/')

@bot.slash_command(name="ping",description="just ping")
async def ping(ctx):
    await ctx.respond(f"{round(ctx.bot.latency*1000)}(ms)")
        
        
    


token=jdata["token"]
bot.run(token)