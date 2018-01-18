import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random


Client = discord.Client()
client = commands.Bot(command_prefix = 'c.')


@client.event
async def on_ready():
    print("Clara is ready!")


@client.event
async def on_message(message):

    await client.change_presence(game=discord.Game(name='Use c.help! >w<'))
    
    if message.content.upper().startswith('C.HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> **O-ou yew need help? OwO Here chu go!!** \n ```Fun Commands~!``` \n ``c.ping`` Pong! :ping_pong: \n ``c.cookie`` Get/give a cookie~! \n ``c.boop`` N-noh using dis command! =3= \n ``2+2=4-1=3`` Jus try it hehe~ \n ``c.rawr`` RAWRRR FEAR MEEEH \n ``c.poi`` P-poi! >^< \n ``c.baka`` B-baka!! \n ``c.hug`` Huuuuggg~! OwO \n ```Server Commands~!``` \n ``c.qotw`` Quote of the week~! \n ``c.gotw`` Gif of de week~! \n ```Membersss OwO``` \n ``c.frost`` Frosty frostttttt =v= \n ``c.benni`` Wonder who yew find here.. OwO \n ``c.nova`` O-ou... wonder who dis ish... QWQ \n ``c.spency`` Ohohooooo leh surprise command hehe" % (userID))

        

    if message.content.upper().startswith ('C.PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong! :ping_pong: " % (userID))

    if message.content.upper().startswith('C.COOKIE'):
        await client.send_message(message.channel, "H-here's a cookie :cookie:")

    if message.content.upper().startswith('C.BOOP'):
        await client.send_message(message.channel, "H-hey! N-noh booping meh nose! >^<")

    if message.content.upper().startswith('2+2=4-1=3'):
        await client.send_message(message.channel, ":OO quick mafs!")
    
    if message.content.upper().startswith('C.RAWR'):
        await client.send_message(message.channel, "RAAWWWRRRRR https://imgur.com/t/rawr/TnAEa5l ")

    if message.content.upper().startswith('C.POI'):
        await client.send_message(message.channel, "P-POIIII!!! >^< https://www.tenor.co/EP1u.gif ")
        
    if message.content.upper().startswith('C.BAKA'):
        await client.send_message(message.channel, "B-ba-ba-baka!!! /)///(\ https://www.tenor.co/xBAy.gif")


        
       
    if message.content.upper().startswith('C.QOTW'):
        Shadow = "275321920575242252"
        await client.send_message(message.channel, "“Frost let me talk woman” ~ <@%s>" % (Shadow))

    if message.content.upper().startswith('C.GOTW'):
        Bambi = "394765184201392128"
        await client.send_message(message.channel, "https://i.imgur.com/ce7BQ8h.gifv ~ from <@%s>" % (Bambi))



    if message.content.upper().startswith('C.HUG'):
        messages = ("https://www.tenor.co/rtUw.gif Huuuuuggu~!", "P-pya~!? H-hug! https://www.tenor.co/MLKl.gif", "https://www.tenor.co/FQNP.gif Hug hug hug!!")
        await client.send_message(message.channel,(random.choice(messages)))
        

    
    if message.content.upper().startswith('C.FROST'):
        Frost = "177185494646521856"
        await client.send_message(message.channel, "“i am become turtle” ~ <@%s>" % (Frost))

    if message.content.upper().startswith('C.BENNI'):
        Benni = "394765184201392128"
        await client.send_message(message.channel, "Ou seems yew found de gif queen <@%s> ~!" % (Benni))

    if message.content.upper().startswith('C.NOVA'):
        Nova = "344856431037775873"
        await client.send_message(message.channel, "All hail de loli goddess * ^ * <@%s>" % (Nova))

    if message.content.upper().startswith('C.SPENCY'):
        Spency = "275739880838135808"
        await client.send_message(message.channel, "https://www.tenor.co/v0Qz.gif Yis yis is de one and only doge <@%s>" % (Spency))

        
client.run("clara-fun bot.py")
           
