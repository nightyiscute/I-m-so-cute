import random
import discord
import json
from discord.ext import commands
from discord.commands import slash_command


class rpg(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    class item():
        def __init__(self,value,rarity,burn_time,type:str):
            self.value=value
            self.rarity=rarity
            self.burn_time=burn_time
            self.type=type
    
    class tool():
        def __init__(self,rarity,durable):
            self.rarity=rarity
            self.durable=durable
    
    Rock=item(20,1,0,"stone")
    Iron=item(40,2,0,"stone")
    RedIron=item(60,2,0,"stone")
    Stone_axe=tool(1,20)
    
    @slash_command(name="成立帳戶")
    async def acc(self,ctx):
        userid = str(ctx.author.id)
        user = ctx.author.name

        with open('thing.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if data.get(userid) is None:
            with open('thing.json', 'w', encoding='utf-8') as jdata:
                data[userid] = {"name":user,"money":100,"rock":0,"iron":0,"RedIron":0,"power":100,"Tool_rarity":0,"Tool_durable":0 }
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            await ctx.respond('帳戶建立成功!')
        else:
            await ctx.respond("你已經有帳戶了")


    @slash_command(name="挖礦")
    

    async def mine(self,ctx):
        ranitem=random.randint(0,100)
        userid = str(ctx.author.id)
        user = ctx.author.name 
        with open('thing.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if data.get(userid) is None:
                await ctx.respond('你還沒有帳戶!,請用 "/成立帳戶" 註冊')
                json.dump(data, jdata, ensure_ascii=False)
                jdata.close()

        else:
            with open('thing.json', 'w', encoding='utf-8') as jdata:
                data[userid]["rock"]+=1
                data[userid]["power"]-=1
                data[userid]["rock"]+=int(ranitem/50)
                await ctx.respond(f"恭喜{user}獲得{int(ranitem/50+1)}個石頭!")
                    

                if data[userid]["Tool_rarity"]>0:
                    data[userid]["iron"]+=int(ranitem/60)
                    data[userid]["Tool_durable"]-=1
                    await ctx.respond(f"恭喜{user}獲得{int(ranitem/60+1)}個鐵礦!")
                json.dump(data,jdata,ensure_ascii=False,sort_keys=True)
                jdata.close()
         
                
            



def setup(bot):
    bot.add_cog(rpg(bot))