import discord
from discord.ext import commands

class Extensions(commands.Cog):
    "⚙️ Deal with extensions"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension: str = commands.parameter(description="- Name of extension in cogs folder")):
        """
        ⚙️ Load an extension 
        
        Example:
        .load test
        """

        await self.bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}.py extension!")
        print(f"Loaded extension: {extension}.py")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension: str = commands.parameter(description="- Name of extension in cogs folder")):
        """
        ⚙️ Unload an extension
        
        Example:
        .unload test
        """

        # Prevents from unloading this extensions.py file itself
        if extension == "extensions":
            await ctx.send("don't do it man, this command comes from this extension :(")
            return

        await self.bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}.py extension!")
        print(f"Unloaded extension: {extension}.py")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension: str = commands.parameter(description="- Name of extension in cogs folder")):
        """
        ⚙️ Reload an extension
        
        Example:
        .reload test
        """

        await self.bot.reload_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}.py extension!")
        print(f"Reloaded extension: {extension}.py")

async def setup(bot):
    await bot.add_cog(Extensions(bot))