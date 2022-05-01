from discord.ext import commands
import os

bot_token = "Enter bot token here"
bot_prefix = '*'


client = commands.Bot(command_prefix=bot_prefix, help_command=None)


@client.event
async def on_ready():
    print("I am working")


for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(bot_token)
