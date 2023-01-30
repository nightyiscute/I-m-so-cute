import random
import discord
from discord.ext import commands
from discord.commands import slash_command

class main(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    option=discord.Option

    nhentai=discord.SlashCommandGroup("nhentai")
    @nhentai.command()
    async def random_num(self,ctx):
        random_int=random.randint(1,999999)
        await ctx.respond(f'https://nhentai.net/g/{random_int}/')
    @nhentai.command()
    async def godnum(self,ctx,num:int,page:option(int,"page",required = False)):
        await ctx.respond(f'https://nhentai.net/g/{num}/{page}')

    @slash_command(name="ping",description="just ping")
    async def ping(self,ctx):
        await ctx.respond(f"{round(ctx.bot.latency*1000)}(ms)")

    
def setup(bot):
    bot.add_cog(main(bot))