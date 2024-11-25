import os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='#', intents=intents)

async def load_cogs():
    for filename in os.listdir('cogs'):
        if filename.endswith('.py'):
            extension = 'cogs.' + filename[:-3]
            print(f"가져온 모듈 : {extension}")
            await bot.load_extension(extension)

@bot.event
async def setup_hook():
    await load_cogs()
    await bot.tree.sync()

@bot.event
async def on_ready():
    print(f'{bot.user}로 준비됨')


bot.run(os.getenv('TOKEN'))
