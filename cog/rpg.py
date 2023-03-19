import random
import discord
import json
from discord.ext import commands
from discord.commands import slash_command


class rpg(commands.Cog):
    option=discord.Option
    def __init__(self,bot):
        self.bot=bot
 
    
            
            

    
    @slash_command(name="成立帳戶")
    async def acc(self,ctx):
        userid = str(ctx.author.id)
        user = ctx.author.name

        with open('thing.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if data.get(userid) is None:
            with open('thing.json', 'w', encoding='utf-8') as jdata:
                data[userid] = {
                    "name":user,
                    "money":100,
                    "rock":0,
                    "iron":0,
                    "wood":0,
                    "RedIron":0,
                    "power":100,
                    "Pick":"hand",
                    "Pick_durable":0,
                    "Pick_level":0,
                    "Axe":"hand",
                    "Axe_durable":0,
                    "Axe_level":0 }
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            await ctx.respond('帳戶建立成功!')
        else:
            await ctx.respond("你已經有帳戶了")


    @slash_command(name="採集")
    

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
                    

                if data[userid]["Pick_level"]>0:
                    data[userid]["rock"]+=int(ranitem/50)
                    data[userid]["iron"]+=int(ranitem/60)
                    if data[userid]["Pick"]!="hand":
                        data[userid]["Pick_durable"]-=1
                    await ctx.respond(f"恭喜{user}獲得{int(ranitem/60+1)}個鐵礦!")

                elif data[userid]["Pick_level"]>1:
                    data[userid]["rock"]+=int(ranitem/40)
                    data[userid]["iron"]+=int(ranitem/50)
                    data[userid]["RedIron"]+=int(ranitem/60)
                    await ctx.respond(f"恭喜{user}獲得{int(ranitem/60+1)}個赤鐵礦!")
                    
                json.dump(data,jdata,ensure_ascii=False,sort_keys=True)
                jdata.close()
         
                
    @slash_command(name="合成")
    async def mix(self,ctx,repices:option(str,"物品",choices=["石鎬","石斧","鐵鎬","鐵斧"])):
        userid = str(ctx.author.id)

        def fast(thing1:str,thing2:str,Tool:str,Tool_level:str,Tool_durable:str,method1:int,method2:int,end_method:str,level:int,ctx):
            with open('thing.json', 'r', encoding='utf-8') as jdata:
                data = json.load(jdata)
                if data[userid][thing1]<method1 or data[userid][thing2]<method2:
                    ctx.respond("材料不夠")
                else:
                    with open("thing.json","w",encoding="utf-8")as jdata:
                        data[userid][thing1]-=method1
                        data[userid][thing2]-=method2
                        data[userid][Tool]=end_method
                        data[userid][Tool_level]=level
                        data[userid][Tool_durable]=50+(level-1)*20
                        ctx.respond(f"恭喜獲得{repices}")
                    
        
        if repices=="石鎬":
            fast("stone","wood","Pick","Pick_level","Pick_durable",3,2,"stone_Pick",1)
        elif repices=="石斧":
            fast("stone","wood","Axe","Axe_level","Axe_durable",3,2,"stone_Axe",1)
        elif repices=="鐵鎬":
            fast("iron","wood","Pick","Pick_level","Pick_durable",3,4,"iron_Pick",2)
        elif repices=="鐵斧":
            fast("iron","wood","Axe","Axe_level","Axe_durable",3,4,"iron_Axe",2)
            
            
        



def setup(bot):
    bot.add_cog(rpg(bot))