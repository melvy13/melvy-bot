import discord
from discord.ext import commands
import math

class Calculator(commands.Cog):
    "🧮 Calculate stuffs up to 4 decimal points"

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, *numbers):
        "➕ Get sum of some numbers [.add {*numbers}]"

        float_list = [float(i) for i in numbers]
        result = sum(float_list)

        expression = " + ".join(numbers)
        await ctx.send(f"{expression} = {result:.4f}")

    @commands.command()
    async def multiply(self, ctx, *numbers):
        "✖️ Get product of some numbers [.multiply {*numbers}]"

        float_list = [float(i) for i in numbers]
        result = math.prod(float_list)

        expression = " x ".join(numbers)
        await ctx.send(f"{expression} = {result:.4f}")

    @commands.command()
    async def minus(self, ctx, number1, number2):
        "➖ Get subtraction of two numbers [.minus {number1} {number2}]"

        result = float(number1) - float(number2)
        expression = number1 + " - " + number2
        await ctx.send(f"{expression} = {result:.4f}")

    @commands.command()
    async def divide(self, ctx, number1, number2):
        "➗ Get division of two numbers [.divide {number1} {number2}]"

        result = float(number1) / float(number2)
        expression = number1 + " ÷ " + number2

        await ctx.send(f"{expression} = {result:.4f}")

    @commands.command()
    async def pi(self, ctx):
        "🥧 Get the value of pi [.pi]"

        await ctx.send("this is pie... no sorry i meant pi. beep boop.")
        await ctx.send("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844" +
                       "609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566" +
                       "923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951" +
                       "941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656")
        
    @commands.command()
    async def euler(self, ctx):
        "   Get the value of Euler's number [.euler]"

        await ctx.send("was π not enough numbers for you? beep boop.")
        await ctx.send("2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413" +
                       "596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800" +
                       "168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443747047230696977" +
                       "20931014169283681902551510865746377211125238978442505695369677078544996996794686445490598793163688923009879312773617821542499")
        
    @commands.command()
    async def sqrt(self, ctx, number):
        "   Get the square root of a number [.sqrt {number}]"

        result = math.sqrt(float(number))
        await ctx.send(f"√{number} = {result:.4f}")

async def setup(bot):
    await bot.add_cog(Calculator(bot))