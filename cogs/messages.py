import discord
from discord.ext import commands
import asyncio

class Messages(commands.Cog):
    "💬 Deal with moderation of messages"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = commands.parameter(description="- Number of messages to clear")):
        """
        🧹 Clear last few messages
        
        Example:
        .clear 10
        """

        await ctx.send(f"Are you sure you want to clear the last {amount} messages? React with 👍 to continue.")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == "👍"
        
        try:
        # Wait for confirmation (timeout after 15 seconds)
            await self.bot.wait_for("reaction_add", check=check, timeout=15.0)
        except asyncio.TimeoutError:
            await ctx.send("beep - Timed out, no messages were deleted.", delete_after=3)
            return
        else:
            await ctx.channel.purge(limit=int(amount)+2) # +2 to also delete the calling message and the confirmation message
            await ctx.send(f"Last {amount} messages have been cleared!", delete_after=3)

async def setup(bot):
    await bot.add_cog(Messages(bot))