import discord
import json
import os
from discord.ext import commands

with open('thing.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)
bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())
      
for file in os.listdir('./cog'):
    if file.endswith('.py'):
        try:
            bot.load_extension(f'cog.{file[:-3]}')
            print(f'{file}加載成功')
        except Exception as error:
            print(f'修{file}時間')

token=jdata["token"]
bot.run(token)