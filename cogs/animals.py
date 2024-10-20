import discord
from discord.ext import commands
import os
import requests
from dotenv import load_dotenv

class Animals(commands.Cog):
    def __init__(self, bot: commands.Bot):
        load_dotenv()
        self.bot = bot
        self.catdog_api_key = os.getenv("CATDOG_APIKEY")

    @commands.command(aliases=["meow"], description="Get random cat pictures... because they are cute... meow")
    async def cat(self, ctx, limit=1):

        if limit > 5:
            await ctx.send("meow meow, meow meow meow (only 5 cat images at a time please) meow meow.. (thank you)")
            return

        url = f"https://api.thecatapi.com/v1/images/search?limit={limit}&api_key={self.catdog_api_key}" # Cat API Call

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if limit == 1:
                if data[0]["url"][-3:] == "gif":
                    await ctx.send("meow meow meow (here is a cute cat gif)")
                else:
                    await ctx.send("meow meow meow (here is a cute cat picture)")
            else:
                await ctx.send("meow meow meow (here are some cute cats)")
            
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

    @commands.command(aliases=["woof"], description="If you can do the same with cats, why not with dogs too? woof")
    async def dog(self, ctx, limit=1):

        if limit > 5:
            await ctx.send("woof woof woof (only 5 dog images at a time please) woof.. (thank you)")
            return
        
        url = f"https://api.thedogapi.com/v1/images/search?limit={limit}&api_key={self.catdog_api_key}" # Dog API Call

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if limit == 1:
                if data[0]["url"][-3:] == "gif":
                    await ctx.send("woof woof (here is a cute dog gif)")
                else:
                    await ctx.send("woof woof (here is a cute dog picture)")
            else:
                await ctx.send("woof woof (here are some cute dogs)")
            
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
    await bot.add_cog(Animals(bot))