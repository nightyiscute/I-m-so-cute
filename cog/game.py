import random
import discord
import json
from discord.ext import commands
from discord.commands import slash_command


class game(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @slash_command(name="比大小",description="比你和機器人誰比較大(?")
    async def 比大小(self,ctx,money:int):
        userid = str(ctx.author.id)
        rannum1=random.randint(0,100)
        rannum2=random.randint(0,100)
        with open('thing.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)
        if rannum1>rannum2:
            with open('thing.json', 'w', encoding='utf-8') as jdata:
                data[userid]["money"]+=money
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            embed=discord.Embed(title="You win!!", color=0x02e328)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            embed.add_field(name=f"你贏了{money}元",value="",inline=False)
            await ctx.respond(embed=embed)
        elif rannum2>rannum1:
            with open('thing.json', 'w', encoding='utf-8') as jdata:
                data[userid]["money"]-=money
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            embed=discord.Embed(title="You win!!", color=0xfa0000)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            embed.add_field(name=f"你輸了{money}元",value="",inline=False)
            await ctx.respond(embed=embed)
        else:
            with open('thing.json', 'w', encoding='utf-8') as jdata:
                data[userid]["money"]+=money*2
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            embed=discord.Embed(title="You win the jackpot!!", color=0xeeff05)
            embed.add_field(name=f"你的數字:{rannum1}", value=f"對方的數字:{rannum2}",inline=False)
            embed.add_field(name=f"你贏了{money*2}元",value="",inline=False)
            await ctx.respond(embed=embed)
        


def setup(bot):
    bot.add_cog(game(bot))
    