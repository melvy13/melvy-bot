import discord
from discord.ext import commands

class Membership(commands.Cog):
    "🧑‍🤝‍🧑 Deal with moderation of members"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = commands.parameter(description="- @Member to kick"), 
                   *, reason: str = commands.parameter(default=None, description="- Reason for kicking")):
        """
        🦵 Kick a member
        
        Example:
        .kick @member I don't like you
        """

        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}! Reason: {reason}")
        print(f"{ctx.author} kicked {member}. Reason: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = commands.parameter(description="- @Member to ban"), 
                   *, reason: str = commands.parameter(default=None, description="- Reason for banning")):
        """
        🔨 Ban a member

        Example:
        .ban @member I hate you
        """

        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}! Reason: {reason}")
        print(f"{ctx.author} banned {member}. Reason: {reason}")

async def setup(bot):
    await bot.add_cog(Membership(bot))