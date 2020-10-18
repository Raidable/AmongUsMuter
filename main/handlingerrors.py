import discord
import asyncio

from commands import m, s
from events import PREFIX
from discord.ext import commands


@m.error
async def muteall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(colour=discord.Colour(0xBD2B2B), description=f"You don't have permissions to use this command!")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(colour=discord.Colour(0xBD2B2B), description=f"{ctx.author.mention} you can use this command every **5** seconds!")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        print("Command Invoke Error, probably the member is trying to use the command while he isn't connected to the channel.")
        embed = discord.Embed(colour=discord.Colour(0xBD2B2B), description=f"{ctx.author.mention} you're not in a **vocal** channel • ⛔️")
        embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ")
        await ctx.send(embed=embed)


@s.error
async def unmuteall_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(colour=discord.Colour(0xBD2B2B), description=f"You don't have permissions to use this command!")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(colour=discord.Colour(0xBD2B2B), description=f"{ctx.author.mention} you can use this command every **5** seconds!")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError):
        print("Command Invoke Error, probably the member is trying to use the command while he isn't connected to the channel.")
        embed = discord.Embed(colour=discord.Colour(0xBD2B2B), description=f"{ctx.author.mention} you're not in a **vocal** channel • ⛔️")
        embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ")
        await ctx.send(embed=embed)
