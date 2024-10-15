import discord
from discord.ext import commands

class Membership(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}! Reason: {reason}")

    @commands.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}! Reason: {reason}")

def setup(bot):
    bot.add_cog(Membership(bot))