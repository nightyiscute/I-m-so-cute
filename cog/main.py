import random
import discord
import json
import datetime
from discord.ext import commands
from discord.commands import slash_command


class main(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    option=discord.Option

    @slash_command(name="ping",description="just ping")
    async def ping(self,ctx):
        await ctx.respond(f"{round(ctx.bot.latency*1000)}(ms)")
    
    @slash_command(name="luck",description="text your luck")
    async def luck(self,ctx):
        random_int=random.randint(0,100)
        if random_int<10:
            random_luck="大凶"
        if 10<=random_int<30:
            random_luck="兇"
        if 30<=random_int<70:
            random_luck="中"
        if 70<=random_int<90:
            random_luck="吉"
        if 90<=random_int:
            random_luck="大吉"

        if random_luck=="大吉":
            lcolor=0x00ff1e
            word="恭喜!今天適合買大樂透"
        if random_luck=="吉":
            lcolor=0x00e1ff
            word="恭喜!今天會有小確幸"
        if random_luck=="中":
            lcolor=0xfbff00
            word="今天運氣不好也不壞，是個平常的一天呢"
        if random_luck=="兇":
            lcolor=0xff8800
            word="今天走路要看路喔，小心踩到狗屎"
        if random_luck=="大凶":
            lcolor=0xff0000
            word="小心血光之災!"
        embed=discord.Embed(title=random_luck,  color=lcolor,timestamp=datetime.datetime.now())
        embed.set_author(name="今日運氣")
        embed.add_field(name=word,value="以上就是占卜結果", inline=False)
        embed.set_footer(text=f"{ctx.author.display_name}占卜於")
        await ctx.respond(embed=embed)

    
def setup(bot):
    bot.add_cog(main(bot))