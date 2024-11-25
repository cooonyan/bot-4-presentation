import os
from discord.ext import commands

class MessageLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        file_path = f'cache/{message.guild.id}.cache'

        if not os.path.exists('cache'):
            os.mkdir('cache')

        with open(file_path, 'a', encoding='utf-8') as f:
            f.write(f'[{message.created_at}] {message.author}: {message.content}\n')

async def setup(bot):
    await bot.add_cog(MessageLogger(bot))
