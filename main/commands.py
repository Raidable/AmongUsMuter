import discord
import asyncio

import datetime
import time


from events import client, PREFIX, IMMAGINETHUMBNAIL, IMMAGINERAID
from discord.ext import commands



#Comando ping
@client.command(enabled=1)
async def ping(ctx):
    embed = discord.Embed(colour=discord.Colour(0xB44704), description=f"**Among US Muter Ping** » ``{round(client.latency * 1000)}ms``")
    embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
    await ctx.send(embed=embed)



#Comando prefix
@client.command(aliases=['prefisso'], enabled=1)
async def prefix(ctx):
    embed = discord.Embed(colour=discord.Colour(0xB44704), description=f"**Among US Muter Prefix** » ``{PREFIX}``")
    embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
    await ctx.send(embed=embed)



@client.command(aliases= ['setup'], enabled=1)
async def help(ctx):
    

    def check1(reaction, user):
        return user != mexcomandi.author and str(reaction.emoji) == '▶️' and reaction.message.id == mexcomandi.id and reaction.count != 1

    def check2(reaction, user):
        return user != mexcomandi2.author and str(reaction.emoji) == '◀️' and reaction.message.id == mexcomandi2.id and reaction.count != 1

    n = 0
    while (True):
        if (n > 0):
            await mexcomandi2.delete()

        embed = discord.Embed(title=f"**💻⠀ AmongUS Muter Command ⠀🔫**\n", colour=discord.Colour(0xB44704), description=f"⠀\n```» What does this BOT do?```\n> **AmongUS Muter** mutes and unmutes **automatically** every user in a **vocal** channel that are in **game**. \n\n```» How can i mute every use in my channel?```\n**➔**⠀.m    ⠀• ⠀ .muteall \n\n```» How can i unmute every user in my channel?```\n**➔** ⠀ .s ⠀ • ⠀.unmuteall\n\n```» What else can it does?```\n**➔**⠀ {PREFIX}commands\n⠀")
        embed.set_thumbnail(url=f"{IMMAGINETHUMBNAIL}")
        embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
        mexcomandi = await ctx.send(embed=embed) 
        await mexcomandi.add_reaction('▶️')
        reaction, user = await client.wait_for('reaction_add', check=check1) 

        if (str(reaction.emoji) == '▶️'):
            await mexcomandi.delete()
            
            embed = discord.Embed(title=f"**💻⠀ Comandi AmongUS Muter ⠀🔫**\n", colour=discord.Colour(0xB44704), description=f"⠀\n```» A cosa serve questo BOT?```\n>⠀**AmongUS Muter** serve a mutare e smutare **automaticamente** tutte le persone in un\ncanale **vocale** che sono in **partita**. \n\n```» Come muto tutte le persone nel mio canale?```\n**➔**⠀.m   ⠀• ⠀ .mutatutti \n\n```» Come smuto tutte le persone nel mio canale?```\n**➔** ⠀ .s ⠀ • ⠀.smutatutti\n\n```» Cosa altro può fare?```\n**➔**⠀ {PREFIX}comandi\n⠀")
            embed.set_thumbnail(url=f"{IMMAGINETHUMBNAIL}")
            embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
            mexcomandi2 = await ctx.send(embed=embed) 
            await mexcomandi2.add_reaction('◀️')
            n =+ 1

            reaction2, user = await client.wait_for('reaction_add', check=check2) 




@client.command(aliases= ['tutorialit'])
async def guida(ctx):

    embed = discord.Embed(colour=discord.Colour(0xB44704), title="\nNon sai come si **gioca**? Nessun problema!", description= "\nClicca [qui](https://justpaste.it/6mkvy) per dare un'occhiata alla **guida**.\n⠀")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764870613286125578/765224503914528828/Among_US_Muter_mini_.jpg")
    embed.set_author(name=f"Hey {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text="Made by Raid#9074 • discord.gg/VSD7M5t", icon_url="https://cdn.discordapp.com/attachments/764870613286125578/765224503914528828/Among_US_Muter_mini_.jpg")

    await ctx.send(embed=embed)



@client.command(aliases= ['tutorialeng', 'tutorial'])
async def guide(ctx):

    embed = discord.Embed(colour=discord.Colour(0xB44704), title="\nDon't you know how to **play**? No problem!", description= "\nClick [here](https://justpaste.it/5q8gp) to take a look at the **guide**.\n⠀")

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/764870613286125578/765224503914528828/Among_US_Muter_mini_.jpg")
    embed.set_author(name=f"Hey {ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
    embed.set_footer(text="Made by Raid#9074 • discord.gg/VSD7M5t", icon_url="https://cdn.discordapp.com/attachments/764870613286125578/765224503914528828/Among_US_Muter_mini_.jpg")

    await ctx.send(embed=embed)




@client.command(enabled=1, aliases=['commands'])
async def comandi(ctx):

    def check1(reaction, user):
        return user != mexcomandi.author and str(reaction.emoji) == '▶️' and reaction.message.id == mexcomandi.id and reaction.count != 1

    def check2(reaction, user):
        return user != mexcomandi2.author and str(reaction.emoji) == '◀️' and reaction.message.id == mexcomandi2.id and reaction.count != 1

    n = 0
    while (True):
        if (n > 0):
            await mexcomandi2.delete()
        embed = discord.Embed(title=f"**⚙️⠀ Among US Muter Commands ⠀🤖**\n", colour=discord.Colour(0x4363BB), description=f"⠀\n**» Important Commands**\n\n``➝ {PREFIX}m | {PREFIX}muteall`` \n\n> **Mutes** every member in the channel.\n\n``➝ {PREFIX}s | {PREFIX}unmuteall`` \n\n> **Unmutes** every member in the channel.\n\n``➝ {PREFIX}prefix`` \n\n> **Shows** the bot's prefix.\n\n``➝ {PREFIX}guide``\n\n> Shows the game **guide**, for new players.\n\n``➝ {PREFIX}map1 | {PREFIX}map2 | {PREFIX}map3``\n\n> Maps introduction.\n⠀")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(url=f"{IMMAGINETHUMBNAIL}")
        embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINETHUMBNAIL}")
        mexcomandi = await ctx.send(embed=embed) 
        await mexcomandi.add_reaction('▶️')
        reaction, user = await client.wait_for('reaction_add', check=check1) 

        if (str(reaction.emoji) == '▶️'):
            await mexcomandi.delete()
            embed = discord.Embed(title=f"**⚙️⠀ Comandi Among US Muter ⠀🤖**\n", colour=discord.Colour(0x4363BB), description=f"⠀\n**» Comandi Rilevanti**\n\n``➝ {PREFIX}m | {PREFIX}mutatutti`` \n\n> Muta tutti i membri nel canale.\n\n``➝ {PREFIX}s | {PREFIX}smutatutti`` \n\n> **Smuta** tutti i membri nel canale.\n\n``➝ {PREFIX}prefix`` \n\n> Mostra il prefisso del bot.\n\n``➝ {PREFIX}guida``\n\n> Mostra la **guida** al gioco, per i nuovi giocatori.\n\n``➝ {PREFIX}map1 | {PREFIX}map2 | {PREFIX}map3``\n\n> Introduzione alle mappe (EN).\n⠀")
            embed.timestamp = datetime.datetime.utcnow()
            embed.set_thumbnail(url=f"{IMMAGINETHUMBNAIL}")
            embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINETHUMBNAIL}")
            mexcomandi2 = await ctx.send(embed=embed) 
            await mexcomandi2.add_reaction('◀️')
            n =+ 1

            reaction2, user = await client.wait_for('reaction_add', check=check2) 



@client.command()
async def map1(ctx):
    await ctx.send(f"**The Skeld** is the primary map of **Among Us**, set on a spaceship. This map was the only one included in the **first version** of the game's launch in **2018**\n\n__Here it is__:\nhttps://cdn.discordapp.com/attachments/764870613286125578/765227479883055124/The-Skeld.png")


@client.command()
async def map2(ctx):
    await ctx.send(f"""Unlike The Skeld, **__MIRA HQ__** is a much __smaller__ and more __intimate__ map.\n\nThis makes it the most **difficult** of the three Among Us maps to win as an **imposter** in a big group. When the round starts, players will either spawn at the **Launchpad** or in the **Cafeteria**.\nThere are only a **few hallways**, meaning you won’t have as much space to run around as you normally would. Additionally, the **Communications** room acts as MIRA HQ’s **Admin room**, allowing players to view a __log__ that constantly updates with each players location. While this might appear to be a downgrade of **The Skeld**’s admin room, it’s actually __perfect__ for tracking an individual person you might be **suspicious** of.
\nAs for **__vents__**, MIRA HQ is rather **unique** since the entire network is connected. There are a total of __**11**__ vents on this map and you can use them to **reach** anywhere on the map. This makes it much **easier** to get away, just be careful as you can easily become **spotted emerging** from one of these __holes__. \n\n__Here it is__:\nhttps://cdn.discordapp.com/attachments/765257375128879105/765259663804596234/2.png""")


@client.command()
async def map3(ctx):
    await ctx.send(f"""The __biggest__ of the __three__ maps in Among Us, **__Polus__** allows players to explore both inside and outside an *arctic base*.\n\n This means there’s a __lot__ of **ground** to cover between rooms, which can be **dangerous** if you’re a crewmate trying to complete your **tasks**. Polus features **__15__** rooms, not counting any of the **decontamination** chambers that are required to go through if you want to enter a __structure__. Similar to **MIRA HQ**, these decontamination rooms will seal someone in for a **few seconds**, denying them access until the doors open.

Additionally, there are **12** vents\n\n__Here it is__:\nhttps://cdn.discordapp.com/attachments/765257375128879105/765260933521211462/POLUS_MAP_GUIDE.png""")

    

@client.command(aliases=['map'])
async def maps(ctx):
    embed = discord.Embed(colour=discord.Colour(0xB44704), description=f"> **The Skeld** »  {PREFIX}map1\n> **MiraHQ** » {PREFIX}map2\n> **Polus** »  {PREFIX}map3\n⠀")
    embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
    await ctx.send(embed=embed)
   



@client.command(aliases= ['muteall'])
#@commands.has_permissions(manage_guild=True)
async def m(ctx):

    canale = ctx.message.author.voice.channel
    i=0
    if (canale != None):
        embed = discord.Embed(colour=discord.Colour(0xB44704), description=f"**Members Muted** • 🔇")
        embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
        await ctx.send(embed=embed)
        while (i<len(canale.members)):
            await canale.members[i].edit(mute=1)
            i+=1

    else:
        embed = discord.Embed(colour=discord.Colour(0x4363BB), title=f"Non sei in un canale **vocale**!")
        await ctx.send(embed=embed)
        
        
@client.command(aliases= ['unmuteall'])
#@commands.has_permissions(manage_guild=True)
async def s(ctx):

    canale = ctx.message.author.voice.channel
    i=0
    if (canale != None):
        embed = discord.Embed(colour=discord.Colour(0xB44704), description=f"**Members UnMuted** • 🔇")
        embed.set_footer(text=f"Made by Raid » discord.gg/VSD7M5t ", icon_url=f"{IMMAGINERAID}")
        await ctx.send(embed=embed)
        while (i<len(canale.members)):
             await canale.members[i].edit(mute=0)
             i+=1
            

    else:
        embed = discord.Embed(colour=discord.Colour(0x4363BB), title=f"Non sei in un canale **vocale**!")
        await ctx.send(embed=embed)
    

    