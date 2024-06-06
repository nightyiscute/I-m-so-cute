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
    
    
    
    @slash_command(name="luck",description="text your luck")
    async def luck(self,ctx):
        userid = int(ctx.author.id)
        today=datetime.datetime.now().strftime("%m%d")
        user_num=userid+int(today)
        def luck_1(num):
            if num==10:
                random_luck="大凶"
            elif 8<=num<=9:
                random_luck="兇"
            elif 3<=num<=7:
                random_luck="中"
            elif 1<=num<3:
                random_luck="吉"
            elif 0<=num:
                random_luck="大吉"
            return random_luck
        if (user_num%3)==0:
            The0Fork=user_num%10
            random_luck=luck_1(The0Fork)
        elif (user_num%3)==1:
            The1Fork=user_num%6*2
            random_luck=luck_1(The1Fork)
        elif (user_num%3)==2:
            The2Fork=user_num%9+5*2-10
            random_luck=luck_1(The2Fork)
            
        if random_luck=="大吉":
            lcolor=0x00ff1e
            word="恭喜!今天適合買大樂透"
        elif random_luck=="吉":
            lcolor=0x00e1ff
            word="恭喜!今天會有小確幸"
        elif random_luck=="中":
            lcolor=0xfbff00
            word="今天運氣不好也不壞，是個平常的一天呢"
        elif random_luck=="兇":
            lcolor=0xff8800
            word="今天走路要看路喔，小心踩到狗屎"
        elif random_luck=="大凶":
            lcolor=0xff0000
            word="小心血光之災!"
            
        embed=discord.Embed(title=random_luck,description=word,color=lcolor, timestamp=datetime.datetime.now())
        embed.set_author(name="今日運氣")
        embed.add_field(name="local", value="", inline=True)
        embed.set_footer(text=f"{ctx.author.display_name}占卜於")
        await ctx.respond(embed=embed)



    @slash_command(name='dice',description='dice number')
    async def dice(self,ctx,number:int):
        ranint=random.randint(1,number)
        embed=discord.Embed(title=ranint, color=discord.Colour.random(), timestamp=datetime.datetime.now())
        embed.set_author(name="骰到的數字是:")
        embed.add_field(name=f"你骰了{number}面骰",value="以上就是骰子結果", inline=False)
        embed.set_footer(text=f"{ctx.author.display_name}骰於")
        await ctx.respond(embed=embed)



    @slash_command(name="計算機",description="就是個計算機")
    async def computer(self,ctx,number1:float,count:option(str,"運算符號",choices=["+","-","*","/","√","^"]),number2:float):
        
        if count=="+":
            embed=discord.Embed(title=number1+number2,color=discord.Colour.random())
            await ctx.respond(embed=embed)

        elif count=="-":
            embed=discord.Embed(title=number1-number2,color=discord.Colour.random())
            await ctx.respond(embed=embed)

        elif count=="*":
            embed=discord.Embed(title=number1*number2,color=discord.Colour.random())
            await ctx.respond(embed=embed)

        elif count=="/":
            embed=discord.Embed(title=number1/number2,color=discord.Colour.random())
            await ctx.respond(embed=embed)
        
        elif count=="^":
            number1a=number1
            for i in range(1,number2):
                number1=number1*number1a
            embed=discord.Embed(title=number1,color=discord.Colour.random())
            await ctx.respond(embed=embed)

        elif count=="√":
            number1a=number1
            for i in range(1,number2):
                number1=number1a**0.5
            embed=discord.Embed(title=number1,color=discord.Colour.random())
            await ctx.respond(embed=embed)

        else:   
            embed=discord.Embed(title="count只有 +,-,*,/,^,√ 喔",color=discord.Colour.random())
            await ctx.respond(embed=embed)
    

    
    @slash_command(name="tag",description="可以用這個tag人")
    async def tag(self,ctx,somebody:discord.Member,times:int):
        if times>20:
            await ctx.respond("冷靜一點啊")
        else:
            for i in range(0,times):
                await ctx.respond(f"{somebody.mention}",delete_after=1)
            
        


    
def setup(bot):
    bot.add_cog(main(bot))