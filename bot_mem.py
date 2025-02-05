import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


def get_animal_image_url():
    urls = ['https://random.dog/woof.json', 'https://random-d.uk/api/random']
    url = random.choice(urls)
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('animal')
async def animal(ctx):
    image_url = get_animal_image_url()
    await ctx.send(image_url)


@bot.command()
async def espri(ctx):
    img_name = random.choice(os.listdir('C:\kodland\Discord Botu\dot3\images'))
    with open(f'C:\kodland\Discord Botu\dot3\images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

bot.run("Token")
