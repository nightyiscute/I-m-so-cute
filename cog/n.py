import random
import json
import discord
from discord.ext import commands
from discord.ui import View,Select

with open('data.json',mode='r',encoding='utf8')as jfile:
    jdata=json.load(jfile)


class n(commands.Cog):
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
        if page=="":
            page=1
        await ctx.respond(f'https://nhentai.net/g/{num}/{page}')

    @nhentai.command()
    async def parody(self,ctx,parody:str):
        await ctx.respond(f"https://nhentai.net/parody/{parody}/")
    
    @nhentai.command()
    async def tag(self,ctx):
        for i in range(143):
            a=i

        tag=discord.ui.Select(
            select_type=discord.ComponentType.string_select,
            placeholder="Choose a tag!", # 沒選選項時
            min_values = 1, # 最少幾個選項
            max_values = 1, # 最多幾個選項
            options = [discord.SelectOption(label=jdata[a][0],description=jdata[a][1])])

        async def select_callback(Select, interaction): #有選選項時
            await interaction.response.send_message(f"https://nhentai.net/tag/{Select.values[0]}/")
        tag.callback=select_callback
        view=View(timeout=0)
        view.add_item(tag)
        await ctx.respond("Choose a flavor!",view=tag())

def setup(bot):
    bot.add_cog(n(bot))