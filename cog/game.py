
import random
import discord
import json
from discord.ext import commands



class game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.slash_command(name="比大小",description="比你和機器人誰比較大(?")
    async def big_or_small(self,ctx):
        rannum1=random.randint(0,100)
        rannum2=random.randint(0,100)
        if rannum1>rannum2:
            embed=discord.Embed(title="You win!!", color=0x02e328)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            await ctx.respond(embed=embed)
        elif rannum2>rannum1:
            embed=discord.Embed(title="You lose!!", color=0xfa0000)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            await ctx.respond(embed=embed)
        else:
            embed=discord.Embed(title="You win the jackpot!!", color=0xeeff05)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            await ctx.respond(embed=embed)
        


def setup(bot):
    bot.add_cog(game(bot))
