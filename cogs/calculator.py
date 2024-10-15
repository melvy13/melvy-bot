import discord
from discord.ext import commands

class Calculator(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="Add numbers with each number separated by a space")
    async def add(self, ctx, *, numbers):
        string_list = numbers.split()
        number_list = [int(i) for i in string_list]
        result = sum(number_list)

        expression = " + ".join(string_list)
        await ctx.send(f"{expression} = {result}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))