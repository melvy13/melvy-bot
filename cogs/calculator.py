import discord
from discord.ext import commands
import math

class Calculator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Add numbers with each number separated by a space")
    async def add(self, ctx, *, numbers):
        string_list = numbers.split()
        number_list = [float(i) for i in string_list]
        result = sum(number_list)

        expression = " + ".join(string_list)
        await ctx.send(f"{expression} = {result}")

    @commands.command(description="Multiply numbers with each number separated by a space")
    async def multiply(self, ctx, *, numbers):
        string_list = numbers.split()
        number_list = [float(i) for i in string_list]
        result = math.prod(number_list)

        expression = " x ".join(string_list)
        await ctx.send(f"{expression} = {result}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))