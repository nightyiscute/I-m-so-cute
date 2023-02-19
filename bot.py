import discord
import json
import os
from discord.ext import commands
from discord.ui import View,Select

with open('thing.json',mode='r',encoding='utf8')as jfile: #打開setting.json,模式是read,命名為jfile
    jdata=json.load(jfile)
bot=commands.Bot(command_prefix="!",intents=discord.Intents.all())
view=discord.ui.View
      
for file in os.listdir('./cog'):
    if file.endswith('.py'):
        try:
            bot.load_extension(f'cog.{file[:-3]}',recursive=True)
            print(f'{file}加載成功')
        except Exception as error:
            print(f'修{file}時間:{error}')
            
@bot.slash_command(name="ping",description="just ping")
async def ping(ctx):
    embed=discord.Embed(title="目前ping值", description=f"{round(ctx.bot.latency*1000)}(ms)", color=discord.Colour.random())
    embed.add_field(name="", value="", inline=False)
    await ctx.respond(embed=embed)
    

@bot.slash_command(description="重載Cog")
async def reload(ctx):
    reload=discord.ui.Select(
        placeholder= "Choose a Cog!", # 沒選選項時選項框上的字
            min_values = 1, # 最少幾個選項
            max_values = 1, # 最多幾個選項
            options = [
                discord.SelectOption(label="n",description="Cog(n)"),
                discord.SelectOption(label="main",description="Cog(main)"),
                discord.SelectOption(label="event",description="Cog(event)")
            ])
    async def callback(interaction): #有選選項時
        bot.reload_extension(f'cog.{reload.values[0]}')
        await interaction.response.send_message(f"{reload.values[0]}載入成功")

    reload.callback = callback   
    view = View(timeout=0)
    view.add_item(reload)  
    await ctx.respond("Choose reload Cog",view=view)


token=jdata["token"]
bot.run(token)