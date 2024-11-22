import discord, os
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix='!')


@bot.tree.command(name='hello', description='testing')  # 명령어 이름, 설명
@app_commands.describe(text1='쓸 내용', text2 = '번호') # 같이 쓸 내용들
async def hello(interaction: discord.Interaction, text1:str, text2:int):    # 출력
    await interaction.response.send_message(f'{interaction.user.mention} : {text1} : {text2}', ephemeral=True)


bot.run(os.getenv('TOKEN'))
