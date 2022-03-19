# first install discord.py
# pip install discord.py
import discord
from discord.ext import commands
import RPi.GPIO as io

led = 3
io.setmode(io.BOARD)
io.setwarnings(False)
io.setup(led,io.OUT)
io.output(led,0)

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print("bot is ready")
    
    
@bot.command()
async def led_on(ctx):
    io.output(led,1)
    await ctx.send("led is on")
    
@bot.command()
async def led_off(ctx):
    io.output(led,0)
    await ctx.send("led is off")
    
    
bot.run("ODY5MjU4MDMzNDU5NDk5MDM4.YP7loQ.dTHJkH81Jgrhi59OjpoRUdkm-As")
