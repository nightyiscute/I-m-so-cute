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

        with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if data.get(userid) is None:
            with open('PlayerData.json', 'w', encoding='utf-8') as jdata:
                data[userid] = {
                    "name":user,
                    "money":100,
                    "power":100,
                    "Ore":{
                    "Rock":0,
                    "Iron_Ore":0,
                    "RedIron":0,
                    "Pick":"hand",
                    "Pick_durable":0,
                    "Pick_level":0
                    },
                    "Wood":{
                    "Wood":0,
                    "Red_Wood":0,
                    "Axe":"hand",
                    "Axe_durable":0,
                    "Axe_level":0
                    },
                    "Today_daliy":0
                     }
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
            await ctx.respond('帳戶建立成功!')
        else:
            await ctx.respond("你已經有帳戶了")



    @slash_command(name="採礦")
    async def mine(self,ctx):
        ranitem=random.randint(0,100)
        userid = str(ctx.author.id)
        user = ctx.author.name 
        with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if data.get(userid) is None:
            await ctx.respond('你還沒有帳戶! \n 請用 "/成立帳戶" 註冊')
            json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
        
        elif userid["power"]<0:
            await ctx.respond("你沒體力了")

        else:
            with open('PlayerData.json', 'w', encoding='utf-8') as jdata:
                data[userid]["Ore"]["Rock"]+=1
                data[userid]["power"]-=1
                data[userid]["Ore"]["Rock"]+=int(ranitem/50)
                Rock=1+int(ranitem/50)
                Iron_Ore=0    
                RedIron=0

                if data[userid]["Ore"]["Pick_level"]>0:
                    data[userid]["Ore"]["Rock"]+=int(ranitem/50)
                    Rock+=int(ranitem/50)
                    data[userid]["Ore"]["Iron_Ore"]+=int(ranitem/60)
                    Iron_Ore+=int(ranitem/60)
                    if data[userid]["Ore"]["Pick"]!="hand":
                        data[userid]["Ore"]["Pick_durable"]-=1
                    

                elif data[userid]["Ore"]["Pick_level"]>1:
                    data[userid]["Ore"]["Rock"]+=int(ranitem/40)
                    data[userid]["Ore"]["Iron_Ore"]+=int(ranitem/50)
                    data[userid]["Ore"]["RedIron"]+=int(ranitem/60)
                    Rock+=int(ranitem/40)
                    Iron_Ore+=int(ranitem/50)
                    RedIron+=int(ranitem/60)

                embed=discord.Embed(title=f"{user}獲得石頭{Rock}塊,鐵礦{Iron_Ore}塊,赤鐵礦{RedIron}塊", color=discord.Colour.random())
                await ctx.respond(embed=embed)
                json.dump(data,jdata,ensure_ascii=False,sort_keys=True)
            jdata.close()



    @slash_command(name="伐木")
    async def wood(self,ctx):
        ranitem=random.randint(0,100)
        userid = str(ctx.author.id)
        user = ctx.author.name 
        with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)

        if data.get(userid) is None:
            await ctx.respond('你還沒有帳戶! \n 請用 "/成立帳戶" 註冊')
            json.dump(data, jdata, ensure_ascii=False)
            jdata.close()

        elif userid["power"]<0:
            await ctx.respond("你沒體力了")

        else:
            with open('PlayerData.json', 'w', encoding='utf-8') as jdata:
                Red_Wood=0
                Wood=0
                data[userid]["Wood"]["Wood"]+=1
                data[userid]["power"]-=1
                data[userid]["Wood"]["Wood"]+=int(ranitem/50)
                Wood+=int(1+ranitem/50)

                if data[userid]["Wood"]["Axe_level"]>0:
                    data[userid]["Wood"]["Wood"]+=int(ranitem/50)
                    Wood+=int(ranitem/50)
                    data[userid]["Wood"]["Red_Wood"]+=int(ranitem/60)
                    Red_Wood+=int(ranitem/60)
                    if data[userid]["Wood"]["Axe"]!="hand":
                        data[userid]["Wood"]["Axe_durable"]-=1
                
                embed=discord.Embed(title=f"{user}獲得木頭{Wood}塊,紅杉木{Red_Wood}塊", color=discord.Colour.random())
                await ctx.respond(embed=embed)
                json.dump(data,jdata,ensure_ascii=False,sort_keys=True)
            jdata.close()      
                


    @slash_command(name="合成")
    async def mix(self,ctx,repices:option(str,"物品",choices=["石鎬","石斧","鐵鎬","鐵斧"])):
        userid = str(ctx.author.id)
        with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)
        if data.get(userid) is None:
            await ctx.respond('你還沒有帳戶! \n 請用 "/成立帳戶" 註冊')
            json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
        else:
            
            if repices=="石鎬":
                Method1="Rock"
                Method2="Wood"
                Tool="Pick"
                level=f"{Tool}_level"
                durable=f"{Tool}_durable"
                Method1_use=3
                Method2_use=2
                End_method=f"{Method1}_{Tool}"
                End_level=1     

            elif repices=="石斧":
                Method1="Rock"
                Method2="Wood"
                Tool="Axe"
                level=f"{Tool}_level"
                durable=f"{Tool}_durable"
                Method1_use=3
                Method2_use=2
                End_method=f"{Method1}_{Tool}"
                End_level=1 

            elif repices=="鐵鎬":
                Method1="Iron_Ore"
                Method2="Red_Wood"
                Tool="Pick"
                level=f"{Tool}_level"
                durable=f"{Tool}_durable"
                Method1_use=3
                Method2_use=4
                End_method=f"{Method1}_{Tool}"
                End_level=2 

            elif repices=="鐵斧":
                Method1="Iron_Ore"
                Method2="Red_Wood"
                Tool="Axe"
                level=f"{Tool}_level"
                durable=f"{Tool}_durable"
                Method1_use=3
                Method2_use=4
                End_method=f"{Method1}_{Tool}"
                End_level=2 

            else:
                await ctx.respond("不存在此配方")

            if Tool=="Axe":
                Tool_Method="Wood"
            else:
                Tool_Method="Ore"

            if data[userid]["Ore"][Method1]<Method1_use or data[userid]["Wood"][Method2]<Method2_use:
                await ctx.respond("材料不夠")
            else:
                with open("PlayerData.json","w",encoding="utf-8")as jdata:
                    data[userid]["Ore"][Method1]-=Method1_use
                    data[userid]["Wood"][Method2]-=Method2_use
                    data[userid][Tool_Method][Tool]=End_method
                    data[userid][Tool_Method][level]=End_level
                    data[userid][Tool_Method][durable]=50+(End_level-1)*20
                    json.dump(data,jdata,ensure_ascii=False,sort_keys=True)     
                jdata.close()
                await ctx.respond(f"恭喜獲得{repices}")    
        


    @slash_command(name="查看物品")
    async def item(self,ctx):
        user=ctx.author.name
        userid = str(ctx.author.id)
        
        with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)
            
        if data[userid]["Ore"]["Pick"]=="hand":
            Output_Pick="手"
        elif data[userid]["Ore"]["Pick"]=="Rock_Pick":
            Output_Pick="石鎬"
        elif data[userid]["Ore"]["Pick"]=="Iron_Ore_Pick":
            Output_Pick="鐵鎬"

        if data[userid]["Wood"]["Axe"]=="hand":
            Output_Axe="手"
        elif data[userid]["Wood"]["Axe"]=="Rock_Axe":
            Output_Axe="石斧"
        elif data[userid]["Wood"]["Axe"]=="Iron_Ore_Axe":
            Output_Axe="鐵斧"
    
        if data[userid]["name"]==user:
            embed=discord.Embed(title="您的包包有:",color=discord.Colour.random())
            embed.add_field(name="石頭:", value=data[userid]["Ore"]["Rock"], inline=False)
            embed.add_field(name="鐵礦", value=data[userid]["Ore"]["Iron_Ore"], inline=False)
            embed.add_field(name="鎬子", value=Output_Pick, inline=False)
            embed.add_field(name="木頭", value=data[userid]["Wood"]["Wood"], inline=False)
            embed.add_field(name="紅杉木", value=data[userid]["Wood"]["Red_Wood"], inline=False)
            embed.add_field(name="斧頭", value=Output_Axe, inline=False)
            embed.add_field(name="neko幣", value=data[userid]["money"], inline=False)
            embed.add_field(name="精力值",value=data[userid]["power"],inline=False)
            await ctx.respond(embed=embed)
        else:
            embed=discord.Embed(title="你他喵還沒申請帳號!!!!!",color=0xff0000)
            await ctx.respond(embed=embed)



    @slash_command(name="每日簽到",description="補充精力值和一些neko幣")
    async def daliy(self,ctx):
        userid=str(ctx.author.id)
        with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
            data = json.load(jdata)
        if data.get(userid) is None:
            await ctx.respond('你還沒有帳戶! \n 請用 "/成立帳戶" 註冊')
            json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
        else:
            if data["New_Day"]==1 and data[userid]["Today_daliy"]==0:
                data[userid]["money"]+=100
                data[userid]["power"]=100
                data[userid]["Today_daliy"]+=1
            else:
                await ctx.respond("你已經簽到過了")  
                




            
        



def setup(bot):
    bot.add_cog(rpg(bot))