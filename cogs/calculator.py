import discord
from discord.ext import commands
import math

class Calculator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Add numbers with each number separated by a space")
    async def add(self, ctx, *numbers):
        float_list = [float(i) for i in numbers]
        result = sum(float_list)

        expression = " + ".join(numbers)
        await ctx.send(f"{expression} = {result}")

    @commands.command(description="Multiply numbers with each number separated by a space")
    async def multiply(self, ctx, *numbers):
        float_list = [float(i) for i in numbers]
        result = math.prod(float_list)

        expression = " x ".join(numbers)
        await ctx.send(f"{expression} = {result}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))