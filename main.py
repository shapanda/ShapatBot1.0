import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^
from keep_alive import keep_alive

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

#Make events

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

    

#make the commands
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

@client.command()
async def shaptodicksmall(ctx):
    await ctx.send("no ur dick is small")

@client.command()
async def socials(ctx):
    await ctx.send("@sardarrah = tiktok")

async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

keep_alive()
token = os.environ.get("TOKEN")
client.run(token)
client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!