import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command(aliases=["hi", "hello", "hey"])
        async def say_hi(ctx):
            await ctx.send(f"Hi, {ctx.author.mention}!")

        @commands.command()
        async def sendembed(ctx):
            embedded_msg = discord.Embed(title="Title of embed", description="Description of embed", color=discord.Color.green())
            embedded_msg.set_thumbnail(url=ctx.author.avatar)
            embedded_msg.add_field(name="Name of field", value="Value of field", inline=False)
            embedded_msg.set_image(url=ctx.guild.icon)
            embedded_msg.set_footer(text="Footer text", icon_url=ctx.author.avatar)
            await ctx.send(embed=embedded_msg)

        @commands.command()
        async def ping(self, ctx):
            ping_embed = discord.Embed(title="Ping", description="Latency in ms", color=discord.Color.blue())
            ping_embed.add_field(name=f"{self.bot.user.name}'s Latency (ms): ", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
            ping_embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar)
            await ctx.send(embed=ping_embed)

async def setup(bot):
    await bot.add_cog(Test(bot))