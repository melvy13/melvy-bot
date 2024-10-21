import discord
from discord.ext import commands
import random
import requests
from dotenv import load_dotenv
import os

class Basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        load_dotenv()
        self.bot = bot
        self.ninjas_api = os.getenv("NINJA_APIKEY")

    @commands.command()
    async def ping(self, ctx):
        "🏓 Ping the bot......or play ping pong [.ping]"
        await ctx.send(f"...pong!\n{(self.bot.latency*1000):.2f}ms")
        print(f"{ctx.message.author} pinged the bot: {(self.bot.latency*1000):.2f}ms")

    @commands.command(name="8ball")
    async def _8ball(self, ctx, *, question):
        "🔮 Roll the magic 8 ball, determine your future [.8ball {question}]"
        responses = ["Yes :D",
                 "Without a doubt :D",
                 "Definitely yes :D",
                 "Absolutely :D",
                 "Certainly :D",
                 "Most likely :)",
                 "No :(",
                 "Don't count on it :(",
                 "Very doubtful :(",
                 "Ask again later :v",
                 "Cannot predict now :v"]
        
        bot_answer = random.choice(responses)
        await ctx.send(f"Rolling the 8 ball...\n\nVerdict: {bot_answer}")
        print(f"{ctx.message.author} rolled the 8 ball.\nQ: {question}\nA: {bot_answer}")

    @commands.command()
    async def rolldice(self, ctx, amount=1):
        "🎲 Roll a dice, or two. Or maybe three. Or maybe more.. [.rolldice {amount (optional)}] "

        dice_art = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        dice = []
        total = 0
        
        for i in range(amount):
            die = random.randint(1, 6)
            dice.append(die)
            await ctx.send(f"{dice_art.get(die)}") # Hashtag in front of text enlarges message in discord

        for die in dice:
            total += die
        await ctx.send(f"You rolled a total of {total}!")

    @commands.command()
    async def choose(self, ctx, *choices):
        "⚖️ Let the bot choose for you, because you can never make decisions [.choice {*choices}]"
        await ctx.send(f"beep - i choose {random.choice(choices)}")

    @commands.command()
    async def quote(self, ctx):
        "📜 Get a random quote"

        url = "https://api.api-ninjas.com/v1/quotes"

        try:
            response = requests.get(url, headers={'X-Api-Key': self.ninjas_api})
            response.raise_for_status()
            data = response.json()

            await ctx.send("beep boop.. here's a random quote:")
            await ctx.send(f"\"{data[0]["quote"]}\" - {data[0]["author"]}")

        except requests.exceptions.HTTPError as http_error:
            await ctx.send(f"beep - http error...\n{http_error}")

        except requests.exceptions.ConnectionError:
            await ctx.send("beep - connection error...")

        except requests.exceptions.Timeout:
            await ctx.send("beep - request timed out...")

        except requests.exceptions.TooManyRedirects:
            await ctx.send("beep - too many redirects...")
        
        except requests.exceptions.RequestException as req_error:
            await ctx.send(f"beep - something unexpected occured...\n{req_error}")

        except Exception as e:
            await ctx.send(f"beep - something went wrong...\n{e}")

async def setup(bot):
    await bot.add_cog(Basic(bot))