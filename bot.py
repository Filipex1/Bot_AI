import discord
from discord.ext import commands
import os, random
import requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachments in ctx.message.attachments:
            file_name = attachments.filename
            file_url = attachments.url
            await attachments.save(f"./{attachments.filename}")
            await ctx.send(f"Zapisano obraz w ./{attachments.filename}")
            await ctx.send(get_class(model="keras_model.h5", labels="labels.txt", image=file_name))
    else:
        await ctx.send("Nie ma żadnego obrazu")

bot.run("MTE5Mjg3Mzc4MzU4NTkzOTYxNw.GdkJ5w.-nT_6Ytbdehplq4VjsmURt8DoHJerBMl1Eo7AU")