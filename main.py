import discord
from discord.ext import commands
from aiohttp import request
bot = commands.Bot(command_prefix='toon ')


@bot.command()
async def ttrdistricts(ctx):
    API = "https://www.toontownrewritten.com/api/population"
    async with request("GET", API, headers={}) as response:
        data = await response.json()
        await ctx.send(data["populationByDistrict"])
        print("did ttrdistricts command successfully")

bot.run("ODU4NDA0NzU2MTY1NDkyNzQ2.YNdpug.DSIPgOe_ljlI4tr_2ttdX9OEvXk")