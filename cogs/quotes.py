import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os

class Quotes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        load_dotenv()
        self.bot = bot
        self.ninjas_api = os.getenv("NINJA_APIKEY")

    @commands.command()
    async def quote(self, ctx):
        "Get a random quote"

        url = "https://api.api-ninjas.com/v1/quotes"

        try:
            response = requests.get(url, headers={'X-Api-Key': self.ninjas_api})
            response.raise_for_status()
            data = response.json()

            await ctx.send("beep boop")
            await ctx.send(f"{data[0]["quote"]} - {data[0]["author"]}")

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
    await bot.add_cog(Quotes(bot))