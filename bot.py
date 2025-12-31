import os
import discord
from discord.ext import commands

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã online: {bot.user}")

# Lệnh ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

# Run bot
bot.run(os.getenv("TOKEN"))
