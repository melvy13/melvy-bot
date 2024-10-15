import discord
from discord.ext import commands
import random

class Basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Pings the bot.....or play ping pong")
    async def ping(self, ctx):
        await ctx.send(f"...pong!\n{(self.bot.latency*1000):.2f}ms")
        print(f"{ctx.message.author} pinged the bot: {(self.bot.latency*1000):.2f}ms")

    @commands.command(name="8ball", description="Roll the magic 8 ball for answering yes/no questions about your future!")
    async def _8ball(self, ctx, *, question):
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
        
        bot_answer = random.choice(responses)
        await ctx.send(f"Rolling the 8 ball...\n\nVerdict: {bot_answer}")
        print(f"{ctx.message.author} rolled the 8 ball.\nQ: {question}\nA: {bot_answer}")

async def setup(bot):
    await bot.add_cog(Basic(bot))