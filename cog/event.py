import random
import json
import discord
from discord.ext import commands


class event(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    
    @commands.Cog.listener()
    async def on_message(self,msg):   
        with open('thing.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
            jdata=json.load(jfile)
    
        if msg.author==self.bot.user:
            return

        if msg.content=="hi":
            random_talk=random.choice(jdata['talk'])
            await msg.channel.respond(random_talk)

        if self.bot.user in msg.mentions:
            WhyTag=[f"tag三小{msg.author.display_name}","有什麼事嗎?",f"在警告你一次{msg.author.display_name}不要再tag偶了!"]
            random_talk=random.choice(WhyTag)
            await msg.channel.respond(random_talk)

        if msg.content=="fuck":
            a1=random.randint(1,100)
            if a1>80:
                await msg.channel.respond("別罵髒話")

def setup(bot):
    bot.add_cog(event(bot))