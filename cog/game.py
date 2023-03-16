import random
import discord
from discord.ext import commands
from discord.commands import slash_command


class game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @slash_command(name="比大小",description="比你和機器人誰比較大(?")
    async def 比大小(self,ctx):
        rannum1=random.randint(0,100)
        rannum2=random.randint(0,100)
        if rannum1>rannum2:
            embed=discord.Embed(title="You win!!", color=0x02e328)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            await ctx.respond(embed=embed)
        elif rannum2>rannum1:
            embed=discord.Embed(title="You lose!!", color=0xe31102)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}", inline=False)
            await ctx.respond(embed=embed)
        else:
            embed=discord.Embed(title="平手?!", color=0x30a4df)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}", inline=False)
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(game(bot))