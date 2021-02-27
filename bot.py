import discord
from discord.ext import commands
from ppadb.client import Client

# All Code to connect to the FireTV

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]

# Where the actual Discord bot Starts

bot = commands.Bot(command_prefix = '$', status=discord.Status.online, activity=discord.Game('With FireTV!'))

@bot.command()
async def stop(ctx):
	await ctx.send('*Stopping* :wave:')
	await bot.logout()

@bot.command()
async def home(ctx):
	device.shell('input keyevent 3')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def up(ctx):
	device.shell('input keyevent 19')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def down(ctx):
	device.shell('input keyevent 20')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def left(ctx):
	device.shell('input keyevent 21')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def right(ctx):
	device.shell('input keyevent 22')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def select(ctx):
	device.shell('input keyevent 66')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def back(ctx):
	device.shell('input keyevent 4')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def next(ctx):
	device.shell('input keyevent 4')
	await ctx.send('***Command has been sent!***')

@bot.command()
async def pause(ctx):
	device.shell('input keyevent 85')
	await ctx.send('***Command has been sent!***')
	
@bot.event
async def on_ready():
    print('Bot is online!')

bot.run("Bot_Token")