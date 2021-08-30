#***************************************************************************#
#                                                                           #
# Toonbot - A Toontown Themed Discord Bot.                                  #
#                                                                           #
#***************************************************************************#
import aiohttp
import box
import datetime
import discord
import json
import random
import os
import platform
import requests
import time

from dadjokes import Dadjoke
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from datetime import datetime
from discord.ext.commands import CommandNotFound

prefix="toon "

intents = discord.Intents.default()
intents.members = True
playing = ["Corporate Crash", "tewtow onlin", "old toontown download free working 100%", "litigator head model", "toontown rewritten field offices leak"]

client = commands.Bot(description="Toonbot", command_prefix=prefix, intents=intents, activity=discord.Game(name=random.choice(playing)))  
client.remove_command('help')


#Owner ID
ownerID = 543576276108181506
owner2ID = 353615061169995779

@client.event
async def on_ready():
  memberCount = len(set(client.get_all_members()))
  serverCount = len(client.guilds)
  print("                                                                ")
  print("################################################################") 
  print(f"            ______                  __          __             ")
  print(f"           /_  __/___  ____  ____  / /_  ____  / /_            ")
  print(f"            / / / __ \/ __ \/ __ \/ __ \/ __ \/ __/            ")
  print(f"           / / / /_/ / /_/ / / / / /_/ / /_/ / /_              ")
  print(f"          /_/  \____/\____/_/ /_/_.___/\____/\__/              ")
  print("                                                                ")
  print("################################################################")
  print("                                                                ")
  print("Running as: " + client.user.name + "#" + client.user.discriminator)
  print(f'With Client ID: {client.user.id}')
  print("\nBuilt With:")
  print("Python " + platform.python_version())
  print("Discord.py " + discord.__version__)

prefix = "toon "


#Help Command
@client.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(color=discord.Color.orange())
    embed.set_author(name="Commands:")

    #General Comamnds
    embed.add_field(
        name="General",
        value=
        "{}help - Shows This Message\n\n {}ping - Says Pong Back To You\n\n {}server - Shows Server Info\n\n {}stats - Show Bot Stats".format(prefix, prefix, prefix, prefix),
        inline=False)

    #Fun Comamnds
    embed.add_field(
        name="Fun",
        value=
        "{}toss - Coin Flip\n\n {}joke - Give a Dad Joke\n\n {}dice - Roll 1-6\n\n {}reverse - Reverses the given text\n\n {}poll <name> - starts a poll".format(prefix, prefix, prefix, prefix, prefix),
        inline=False)
    embed.add_field(
        name="Reddit Commands",
        value="{}meme - Gives a random meme from r/memes.\n\n {}r/toontown - shows a random post from the Toontown subreddit.\n\n {}r/toontownrewritten - shows a random post from the Toontown Rewritten subreddit.".format(prefix, prefix, prefix),
        inline=False)

    await ctx.send(author, embed=embed)



#Ping Command
@client.command()
async def ping(ctx):
    """Ping Pong"""
    await ctx.send('Pong!')


#Roll Dice Command
@client.command(aliases=["roll"])
async def dice(ctx):
    """Rolls the dice"""
    cont = random.randint(1, 6)
    await ctx.send("You Rolled **{}**".format(cont))


#Coin Flip Command
@client.command(aliases=["flip"])
async def toss(ctx):
    """Put the toss"""
    ch = ["Heads", "Tails"]
    rch = random.choice(ch)
    await ctx.send(f"You got **{rch}**")


#Reverse Text Command
@client.command()
async def reverse(ctx, *, text):
    """Reverse the given text"""
    await ctx.send("".join(list(reversed(str(text)))))


#Meme Command
@client.command()
async def meme(ctx):
    """Sends you random meme"""
    r = await aiohttp.ClientSession().get(
        "https://www.reddit.com/r/dankmemes/top.json?sort=new&t=day&limit=100")
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)


#r/Toontown Command Command
@client.command(aliases=['r/toontown'])
async def rtoontown(ctx):
    """Sends you a random post from r/toontown"""
    r = await aiohttp.ClientSession().get(
        "https://www.reddit.com/r/toontown.json?sort=new&t=day&limit=100")
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)

#r/ToontownRewritten Command Command
@client.command(aliases=['r/toontownrewritten'])
async def rtoontownrewritten(ctx):
    """Sends you a random post from r/toontownrewritten"""
    r = await aiohttp.ClientSession().get(
        "https://www.reddit.com/r/toontownrewritten.json?sort=new&t=day&limit=100")
    r = await r.json()
    r = box.Box(r)
    data = random.choice(r.data.children).data
    img = data.url
    title = data.title
    url_base = data.permalink
    url = "https://reddit.com" + url_base
    embed = discord.Embed(title=title, url=url, color=discord.Color.blurple())
    embed.set_image(url=img)
    await ctx.send(embed=embed)

#Dadjoke Command
@client.command(aliases=["dadjoke"])
async def joke(ctx):
    """Sends the dadjokes"""
    async with ctx.typing():
        await ctx.send(Dadjoke().joke)

@client.command("server")
async def s_info(ctx):
    server = ctx.guild
    icon = ("\uFEFF")
    embed = discord.Embed(
        title=f"Server info for {server.name}",
        description='\uFEFF',
        colour=0x98FB98,
        timestamp=ctx.message.created_at)
    embed.set_thumbnail(url=server.icon_url_as(size=256))
    embed.add_field(name="Name", value=server.name, inline=True)
    embed.add_field(name="Region", value=server.region, inline=True)
    embed.add_field(name="Member Count", value=server.member_count, inline=True)
    embed.add_field(name="Owner", value="<@" + f"{server.owner_id}" + ">", inline=True)
    embed.add_field(name="ID", value=server.id, inline=True)
    embed.add_field(name="Creation Date", value=f"{server.created_at}", inline=True)
    embed.add_field(name="Server Icon Url", value=server.icon_url, inline=True)
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    await ctx.send(content=None, embed=embed)

#Stats Command
@client.command()
async def stats(ctx):

    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(
        title=f'{client.user.name} Stats',
        description='\uFEFF',
        colour=0x98FB98,
        timestamp=ctx.message.created_at)

    embed.add_field(
        name='Python Version:', value=f"{pythonVersion}", inline=False)
    embed.add_field(
        name='Discord.py Version', value=f"{dpyVersion}", inline=False)
    embed.add_field(name='Total Guilds:', value=f"{serverCount}", inline=False)
    embed.add_field(name='Total Users:', value=f"{memberCount}", inline=False)
    embed.add_field(name='Bot Developers:', value="<@" + f"{ownerID}" + ">, " "<@" + f"{owner2ID}" + ">", inline=False)
    embed.set_footer(text=f"Yours truly, {client.user.name}")
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)

    await ctx.send(embed=embed)


#Poll Command
@client.command(pass_context=True)
async def poll(ctx, *args):
    mesg = ' '.join(args)
    embed = discord.Embed(
        title='A Poll has Started !',
        description='{0}'.format(mesg),
        color=0x00FF00)

    embed.set_footer(text='Poll created by: {0} • React to vote!'.format(
        ctx.message.author))

    embed_message = await ctx.send(embed=embed)

    await embed_message.add_reaction('👍')
    await embed_message.add_reaction('👎')
    await embed_message.add_reaction('🤷')

#TTRDistricts commands
@client.command(pass_context=True)
async def ttrdistricts(ctx):
    ttr_districts_api = "https://www.toontownrewritten.com/api/population"
    ttr_districts_response = requests.get(ttr_districts_api, verify=True)
    ttr_districts_json = ttr_districts_response.json()
    ttr_districts = ttr_districts_json["populationByDistrict"]
    ttr_districts = json.dumps(ttr_districts, sort_keys=True, indent=2)
    ttr_districts = ttr_districts.replace('"', '')
    ttr_districts = ttr_districts.replace(',', '')
    ttr_districts = str(ttr_districts)[1:-2]
    
    await ctx.send(ttr_districts)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("That Command Was not found!")



#Run Bot
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)
