from discord.ext import commands, tasks
import discord
import requests

url = 'http://shibe.online/api/shibes?count=1'

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

BOT_TOKEN = ""


@bot.command()
async def bird(ctx):
  url = 'http://shibe.online/api/birds?count=1'
  response = requests.get(url)
  text1 = response.text
  text2 = text1.replace('[', ' ')
  text3 = text2.replace(']', ' ')
  image = text3.replace('"', ' ')

  await ctx.send('Here is your bird:')
  await ctx.send(image)

@bot.command()
async def cat(ctx):
  url = 'http://shibe.online/api/cats?count=1'
  response = requests.get(url)
  text1 = response.text
  text2 = text1.replace('[', ' ')
  text3 = text2.replace(']', ' ')
  image = text3.replace('"', ' ')

  await ctx.send('Here is your cat:')
  await ctx.send(image)

@bot.command()
async def doge(ctx):
  url = 'http://shibe.online/api/shibes?count=1'
  response = requests.get(url)
  text1 = response.text
  text2 = text1.replace('[', ' ')
  text3 = text2.replace(']', ' ')
  image = text3.replace('"', ' ')

  await ctx.send('Here is your shibe:')
  await ctx.send(image)


bot.run(BOT_TOKEN)
