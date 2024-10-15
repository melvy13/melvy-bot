from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import random

# Load bot token
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot presence
game = discord.Game("with the API...")

initial_extensions = ["cogs.test"]

class melvyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."), 
            intents=intents
        )

    async def on_ready(self):
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

    async def initialize_cogs(self):
        for ext in initial_extensions:
            await self.load_extension(ext)
            print(f"Loaded extension {ext}!")

bot = melvyBot()

@bot.command()
async def ping(ctx):
    await ctx.send(f"...pong!\n\nor did you want the latency? : {(bot.latency*1000):.2f}ms")

@bot.command(aliases=["8ball", "eightball", "magiceightball"])
async def magic8ball(ctx, *, question):
    responses = ["Yes :D",
                 "Without a doubt :D",
                 "Definitely yes :D",
                 "Absolutely :D",
                 "Certainly :D",
                 "Most likely :)",
                 "No :(",
                 "Don't count on it :(",
                 "Very doubtful :(",
                 "Ask again later :v",
                 "Cannot predict now :v"]
    
    await ctx.send(f"Your question: {question}\nBot answer: {random.choice(responses)}")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)