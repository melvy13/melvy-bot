import discord
from discord.ext import commands

class Extensions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(description="")
    async def load(self, ctx, extension):
        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}.py extension!")
        print(f"Loaded extension: {extension}.py")

    @commands.command(description="Unload an extension")
    async def unload(self, ctx, extension):
        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}.py extension!")
        print(f"Unloaded extension: {extension}.py")

    @commands.command(description="Reload an extension")
    async def reload(self, ctx, extension):
        await self.bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}.py extension!")
        print(f"Reloaded extension: {extension}.py")

async def setup(bot):
    await bot.add_cog(Extensions(bot))