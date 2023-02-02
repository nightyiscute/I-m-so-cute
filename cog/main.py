import random
import discord
import json
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
        options = [ # 選項
            discord.SelectOption(label=jdata[i],description=jdata[i][1]),
            ]
        )
        async def select_callback(self, select, interaction): # the function called when the user is done selecting options
            await interaction.response.send_message(f"https://nhentai.net/tag/{select.values[0]}/")

class main(commands.Cog):

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

    @slash_command(name="ping",description="just ping")
    async def ping(self,ctx):
        await ctx.respond(f"{round(ctx.bot.latency*1000)}(ms)")
    
    

    
def setup(bot):
    bot.add_cog(main(bot))