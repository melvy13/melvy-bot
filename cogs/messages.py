import discord
from discord.ext import commands

class Messages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Clear the last 6 messages (including calling command) unless specfied")
    async def clear(self, ctx, amount=6):
        await ctx.channel.purge(limit=amount)

async def setup(bot):
    await bot.add_cog(Messages(bot))