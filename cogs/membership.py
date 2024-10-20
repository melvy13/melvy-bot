import discord
from discord.ext import commands

class Membership(commands.Cog):
    "🧑‍🤝‍🧑 Deal with moderation of members"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        "🦵 Kick a member [.kick {@member} {reason (optional)}]"

        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}! Reason: {reason}")
        print(f"{ctx.author} kicked {member}. Reason: {reason}")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        "🔨 Ban a member [.ban {@member} {reason (optional)}]"

        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}! Reason: {reason}")
        print(f"{ctx.author} banned {member}. Reason: {reason}")

async def setup(bot):
    await bot.add_cog(Membership(bot))