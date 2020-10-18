import discord
import asyncio
import json

from discord.ext import commands




#---CONFIG FETCH---
with open("..\config.json") as f:
    f = json.load(f)
    

PREFIX = f.get("PREFIX")
TOKEN = f.get("TOKEN BOT")

intents = discord.Intents(messages=True, members= True, guilds=True, reactions= True, voice_states=True, presences=True)
   
client = commands.Bot(command_prefix=PREFIX, help_command=None, intents=intents)


IMMAGINERAID = "https://cdn.discordapp.com/attachments/689601069025722369/745777331335069716/immagine.jpg"
IMMAGINETHUMBNAIL = "https://cdn.discordapp.com/attachments/765257375128879105/765268822831005726/Among_US_Muter_mini_-removebg-preview.png"


@client.event
async def on_ready():
    client.loop.create_task(cambio_stato())
    print ("""
    
░█████╗░███╗░░░███╗░█████╗░███╗░░██╗░██████╗░  ██╗░░░██╗░██████╗  ███╗░░░███╗██╗░░░██╗████████╗███████╗██████╗░
██╔══██╗████╗░████║██╔══██╗████╗░██║██╔════╝░  ██║░░░██║██╔════╝  ████╗░████║██║░░░██║╚══██╔══╝██╔════╝██╔══██╗
███████║██╔████╔██║██║░░██║██╔██╗██║██║░░██╗░  ██║░░░██║╚█████╗░  ██╔████╔██║██║░░░██║░░░██║░░░█████╗░░██████╔╝
██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██║░░╚██╗  ██║░░░██║░╚═══██╗  ██║╚██╔╝██║██║░░░██║░░░██║░░░██╔══╝░░██╔══██╗
██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║╚██████╔╝  ╚██████╔╝██████╔╝  ██║░╚═╝░██║╚██████╔╝░░░██║░░░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═════╝░  ╚═╝░░░░░╚═╝░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝\n
\n
 ______     __   __    
/\  __ \   /\ "-.\ \   
\ \ \/\ \  \ \ \-.  \  
 \ \_____\  \ \_  "\_\ 
  \/_____/   \/_/ \/_/ 
                       
                                                     
\ndiscord.gg/VSD7M5t
Raid#9074
\nWatch the Bot video and read README.md
""")



async def cambio_stato():
    while True:
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name = "AmongUS with friends", type = discord.ActivityType.playing), afk=False)
        await asyncio.sleep(5)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(name = f"{PREFIX}help • {PREFIX}commands", type = discord.ActivityType.watching), afk=False)
        await asyncio.sleep(5)




