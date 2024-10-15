from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load bot token
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

bot.run(BOT_TOKEN)