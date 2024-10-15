from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import asyncio

# Load bot token
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot presence status
game = discord.Game("with the API...")

initial_extensions = ["extensions", "membership", "basic", "messages"]

class melvyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."), 
            intents=intents
        )

    async def on_ready(self):
        print("--------------------")
        print(f"Beep boop {self.user} is online and ready!")
        print("--------------------")
        await self.change_presence(activity=game)
        
    async def on_member_join(self, member: discord.Member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Hi {member.mention}! Welcome to {guild.name}!"
            await guild.system_channel.send(to_send)
            print(f"{member} has joined >.>")

    async def on_member_remove(self, member: discord.Member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f"Bye, {member.mention}!"
            await guild.system_channel.send(to_send)
            print(f"{member} has left :C")

bot = melvyBot()

async def load_initial_extensions():
    for file in initial_extensions:
        await bot.load_extension(f"cogs.{file}")
        print(f"Loaded initial extension: {file}.py")

async def main():
    async with bot:
        await load_initial_extensions()
        await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())