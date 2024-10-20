import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv

class Cat(commands.Cog):
    def __init__(self, bot: commands.Bot):
        load_dotenv()
        self.bot = bot
        self.cat_api_key = os.getenv("CAT_APIKEY")

    @commands.command(aliases=["meow"], description="Get random cat pictures... because they are cute... meow")
    async def cat(self, ctx, limit=1):

        if limit > 5:
            await ctx.send("meow meow, meow meow meow (only 5 cat images at a time please) meow meow.. (thank you)")
            return

        url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&api_key={self.cat_api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            print(data)

            await ctx.send("meow meow meow (here are your cute cat pictures)")
            for i in range(limit):
                await ctx.send(data[i]["url"])

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
    await bot.add_cog(Cat(bot))