import random
import json
import discord
from discord.ext import commands
from discord.commands import slash_command


with open('data.json',mode='r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

for i in range(143):
    a=i
    
class tag(discord.ui.View):
    @discord.ui.select( 
    tag = "Choose a tag!", # the placeholder text that will be displayed if nothing is selected
    min_values = 1, # 最少幾個選項
    max_values = 1, # 最多幾個選項
    options = [discord.SelectOption(label=jdata[a][0],description=jdata[a][1])])
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options
        await interaction.response.send_message(f"https://nhentai.net/tag/{select.values[0]}/")

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
        await ctx.respond(f'https://nhentai.net/g/{num}/{page}')

    @nhentai.command()
    async def parody(self,ctx,parody:str):
        await ctx.respond(f"https://nhentai.net/parody/{parody}/")
    
    @nhentai.command()
    async def tag(self,ctx):
        await ctx.respond("Choose a flavor!",view=tag())

def setup(bot):
    bot.add_cog(n(bot))