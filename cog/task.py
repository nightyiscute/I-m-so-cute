import discord
import datetime
import json
from discord.ext import commands,tasks



class Task(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot=bot
        self.daliy_check.start()
        self.check_num=0

@tasks.loop(minutes=4.0)
async def daliy_check(self):
    T=datetime.datetime.now().strftime("%H%M")
    if T-2356>=-4 and T-0000<=4:
        self.check_num =1
        if self.check_num>1:
            self.check_num=0
            return
        else:
            with open('PlayerData.json', 'r', encoding='utf-8') as jdata:
                data = json.load(jdata)
            with open("PlayerData.json","w",encoding='utf-8') as jdata:
                data["New_Day"]=1
                json.dump(data, jdata, ensure_ascii=False)
            jdata.close()
        
