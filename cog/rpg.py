import random
import discord
import json
from discord.ext import commands
from discord.commands import slash_command


class rpg(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    class ore():
        def __init__(self,value,rarity):
            self.value=value
            self.rarity=rarity
    
    rock=ore(20,1)
    iron=ore(40,2)
    RedIron=ore(60,2)
    
    @slash_command(name="成立帳戶")
    async def acc(self,ctx):
        userid = str(ctx.author.id)
        user = ctx.author.name

        with open('data.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if jdata.get(userid) is None:
            with open('data.json', 'w', encoding='utf-8') as jdata:
                data[userid] = {"name":user,"money":100,"rock":0,"iron":0,"RedIron":0,"power":100 }
            json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            await ctx.respond('帳戶建立成功!')
        else:
            await ctx.respond("你已經有帳戶了")


    @slash_command(name="挖礦")
    

    async def mine(self,ctx):
        ranore=random.randint(0,100)
        userid = str(ctx.author.id)
        user = ctx.author.name 
        with open('data.json', 'r', encoding='utf-8') as jdata:
          data = json.load(jdata)

        if jdata.get(userid) is None:
            await ctx.respond('你還沒有帳戶!,請用 "/成立帳戶" 註冊')
        else:
            data[userid]["rock"]+=1
            data[userid]["power"]-=1
            data[userid]["rock"]+=ranore/50
            await ctx.respond(f"恭喜{user}獲得{ranore/50+1}個石頭!")
            



def setup(bot):
    bot.add_cog(rpg(bot))