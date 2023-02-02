import random
import discord
from discord.ext import commands
from discord.commands import slash_command

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

    class tag(discord.ui.View):
        @discord.ui.select( 
        tag = "Choose a tag!", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # 最少幾個選項
        max_values = 1, # 最多幾個選項
        options = [ # 選項
            discord.SelectOption(label="kissing",description="接吻"),
            discord.SelectOption(label="masturbation",description="自慰"),
            discord.SelectOption(label="sole action",description="自慰"),
            discord.SelectOption(label="fingering",description="手指"),
            discord.SelectOption(label="handjob",description="打手槍"),
            discord.SelectOption(label="bukkake",description="顏射"),
            discord.SelectOption(label="blowjob",description="口交"),
            discord.SelectOption(label="gokkun",description="吞精"),
            discord.SelectOption(label="cunnilingus",description="舔陰"),
            discord.SelectOption(label="paizuri",description="乳交"),
            discord.SelectOption(label="footjob",description="足交"),
            discord.SelectOption(label="sumata",description="大腿交"),
            discord.SelectOption(label="leg lock",description="腳夾住對方"),
            discord.SelectOption(label="nakadashi",description="內射"),
            discord.SelectOption(label="squirting",description="潮吹"),
            discord.SelectOption(label="anal",description="肛門"),
            discord.SelectOption(label="anal intercourse",description="肛交"),
            discord.SelectOption(label="bdsm",description="BDSM"),
            discord.SelectOption(label="humiliation",description="羞辱"),
            discord.SelectOption(label="body writing",description="在身體寫字"),
            discord.SelectOption(label="bondage",description="綁縛"),
            discord.SelectOption(label="shibari",description="綁縛"),
            discord.SelectOption(label="orgasm denial",description="禁止高潮"),
            discord.SelectOption(label="human pet",description="寵物玩法"),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            discord.SelectOption(label="",description=""),
            

            
        ]
        )
        async def select_callback(self, select, interaction): # the function called when the user is done selecting options
            await interaction.response.send_message(f"https://nhentai.net/tag/{select.values[0]}/")
    @nhentai.command()
    async def flavor(self,ctx):
        await ctx.respond("Choose a flavor!",view=tag())

    @slash_command(name="ping",description="just ping")
    async def ping(self,ctx):
        await ctx.respond(f"{round(ctx.bot.latency*1000)}(ms)")
    
    

    
def setup(bot):
    bot.add_cog(main(bot))