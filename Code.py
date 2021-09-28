import keep_alive
import discord
import os
import random
import secrets
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import logging
from discord.utils import find
import requests
from datetime import datetime
import pytz


bot = commands.Bot(command_prefix='!')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.members = True

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The Fat And The Curious XIII"))

@client.event
async def on_message(message):
  if message.author == client.user:
   return
   
  if "Fuck" in message.content:
    msg = "why such a need for this strong word huh? Mister {0.author.mention}.".format(message)
    await message.channel.send(msg)
 
  if "fuck" in message.content:
    msg = "why such a need for this strong word huh? Mister {0.author.mention}.".format(message)
    await message.channel.send(msg)
   
  if "FUCK" in message.content:
    msg = "why such a need for this strong word huh? Mister {0.author.mention}.".format(message)
    await message.channel.send(msg)
   
  if "quote" in message.content:
    foo = ["Your mind will answer most questions if you learn to relax and wait for the answer - William Burroughs", "I have so much chaos in my life, it's become normal. You become used to it. You have to just relax, calm down, take a deep breath and try to see how you can make things work rather than complain about how they're wrong. - Tom Welling", "Sometimes letting things go is an act of far greater power than defending or hanging on. - Eckhart Tolle"]
    await message.channel.send(secrets.choice(foo))
   
  if "tanks" in message.content:
    await message.delete()
 
  if "Tanks" in message.content:
    await message.delete()
   
  if "!vote" in message.content:
    await message.channel.send("Please vote for our server at ( https://top.gg/servers/858345099302010900 ) Thanks for voting")
   
  if message.content.startswith("no"):
    await message.channel.send("shut up")

  if message.content.startswith("No"):
    await message.channel.send("shut up")
 
  if "bot" in message.content:
    msg = " {0.author.mention}, talking to me?".format(message)
    await message.channel.send(msg)
 

  if "hello" in message.content:
    foo = ["{0.author.mention} not you again", "{0.author.mention} he's back!", "{0.author.mention} I didn't know you would be back", "hello {0.author.mention}", "look who's back {0.author.mention}", "we sincerely do not care {0.author.mention}"]
    msg = secrets.choice(foo).format(message)
    await message.channel.send(msg)

  if "Hello" in message.content:
    foo = ["{0.author.mention} not you again", "{0.author.mention} he's back!", "{0.author.mention} I didn't know you would be back", "hello {0.author.mention}", "look who's back {0.author.mention}", "we sincerely do not care {0.author.mention}"]
    msg = secrets.choice(foo).format(message)
    await message.channel.send(msg)

 
  if "shut up" in message.content:
    foo = ["Hello {0.author.mention}, I can see you're quite stressed out, here's a video on how to relax: https://www.youtube.com/watch?v=CQjGqtH-2YI", "According to google ({0.author.mention}) the word stupid means -Shut up is a direct command with a meaning very similar to be quiet, but which is commonly perceived as a more forceful command to stop making noise or otherwise communicating, such as talking. The phrase is probably a shortened form of shut up your mouth or shut your mouth up. So mister 'clever person {0.author.mention}' what do you think now?", "could you do all of us a favor '{0.author.mention}' and please do exactly as you said in the message above", "{0.author.mention} do you want to fight?"]
    msg = secrets.choice(foo).format(message)
    await message.channel.send(msg)
   
  if "Shut up" in message.content:
    foo = ["Hello {0.author.mention}, I can see you're quite stressed out, here's a video on how to relax: https://www.youtube.com/watch?v=CQjGqtH-2YI", "According to google ({0.author.mention}) the word stupid means -Shut up is a direct command with a meaning very similar to be quiet, but which is commonly perceived as a more forceful command to stop making noise or otherwise communicating, such as talking. The phrase is probably a shortened form of shut up your mouth or shut your mouth up. So mister 'clever person {0.author.mention}' what do you think now?", "could you do all of us a favor '{0.author.mention}' and please do exactly as you said in the message above", "{0.author.mention} do you want to fight?"]
    msg = secrets.choice(foo).format(message)
    await message.channel.send(msg)

  if message.content.startswith("!Earth Bot"):
    foo = ["Oh, thanks for asking. I am a discord bot, and my only purpose is to make your server more 'fun'. I mean, kinda, I'm a little bit annoying too, but that doesn't matter. Created by the clever and genius person 'Strumber'.", "I am Earth Bot, a discord bot designed to be great with servers, and be great at being annoying, created by the one and only 'Strumber'"]
    msg = secrets.choice(foo).format(message)
    await message.channel.send(msg)

  if "!help" in message.content:
    embedVar = discord.Embed(title="**Earth Bot**", description="The following commands that can be used with the bot are: \n \n !vote - Let's you vote for the Earth server \n hello - Answers you with different responses \n no - Tells you to shut up \n shut up - Answers with multiple different answers \n quote - Gives a random quote \n fuck - You try that out \n !Earth Bot - Description of bot and creator \n bot - answers with a response, you can try it out \n !laugh - sends laughing emojis", color=0x00ff00)
    embedVar.add_field(name="**Time Commands**", value="Do *!time commands* to see time commands you can do", inline=False)
    embedVar.add_field(name="**Purpose**", value="The only point of this bot is to be annoying, great for servers that want some fun in them)", inline=False)
    embedVar.add_field(name="DM Welcome Bot", value="https://bit.ly/3xsl9HQ", inline=False)
    embedVar.add_field(name="**Bot Links**", value="Earth Bot - https://bit.ly/3hlxYhi \n Earth Bot Welcomer - https://bit.ly/3xsl9HQ", inline=False)
    await message.channel.send(embed=embedVar)

  if "!time commands" in message.content:
    embedVar = discord.Embed(title="**Time Commands**", description="There are a couple of time commands to use with the bot, the command starts with **!time** and then the capital. \n Ex. *!time ny*:", color=0xADD8E6)
    embedVar.add_field(name="**!time**", value="!time ny - New York \n !time london - London \n !time madrid - Madrid \n !time canberra - Canberra \n !time kabul - Kabul \n !time buenos aires - Buenos Aires \n !time brussels - Brussels \n !time dhaka - Dhaka \n !time sofia - Sofia \n !time copenhagen - Copenhagen", inline=False)
    await message.channel.send(embed=embedVar)

  if "!me" in message.content:
    msg = " {0.author.mention} ".format(message)
    embedVar = discord.Embed(title= "User", description=(msg), color=0xADD8E6)
    msg2 = "{0.author.mention}".format(message)
    embedVar.add_field(name= (msg2), value= "ID", inline=True)
    await message.channel.send(embed=embedVar)

  if "!m2" in message.content:
    msg = " {0.author.mention}, talking to me?".format(message)
    await message.channel.send(msg)

  if "!laugh" in message.content:
    await message.channel.send("😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂😂")
    
  if "funny" in message.content:
    msg = "that's quite funny".format(message)
    await message.channel.send(msg)

  if message.content.startswith('!servers'):
    embedVar = discord.Embed(title="**I'm currently sitting in " + str(len(client.guilds)) + " servers!**", color=0xFFFF00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!archie'):
    embedVar = discord.Embed(title="Archie", description= "Archie, Is a one of a kind species, most of the time in it's natural habitat, munching on some food. \n He's notorious for being extraordinarily dumb, and stupid. These species are in grave danger due to it's low popularity \n 'I don't like kids. -Archie'", color=0xFFFF00)
    await message.channel.send(embed=embedVar)
 
  if message.content.startswith('!time ny'):
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.now(tz_NY)
    msg = datetime_NY.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in New York is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time london'):
    tz_London = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    msg = datetime_London.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="Oi bruv, the current time in London is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time madrid'):
    tz_Madrid = pytz.timezone('Europe/Madrid')
    datetime_Madrid = datetime.now(tz_Madrid)
    msg = datetime_Madrid.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Madrid is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)
    
  if message.content.startswith('!time canberra'):
    tz_Canberra = pytz.timezone('Australia/Canberra')
    datetime_Canberra = datetime.now(tz_Canberra)
    msg = datetime_Canberra.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Canberra is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time kabul'):
    tz_Kabul = pytz.timezone('Asia/Kabul')
    datetime_Kabul = datetime.now(tz_Kabul)
    msg = datetime_Kabul.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Kabul is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time buenos aires'):
    tz_AR = pytz.timezone('America/Argentina/Buenos_Aires')
    datetime_AR = datetime.now(tz_AR)
    msg = datetime_AR.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Buenos Aires is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time brussels'):
    tz_BE = pytz.timezone('Europe/Brussels')
    datetime_BE = datetime.now(tz_BE)
    msg = datetime_BE.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Brussels is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time dhaka'):
    tz_BD = pytz.timezone('Asia/Dhaka')
    datetime_BD = datetime.now(tz_BD)
    msg = datetime_BD.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Dhaka is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time sofia'):
    tz_BG = pytz.timezone('Europe/Sofia')
    datetime_BG = datetime.now(tz_BG)
    msg = datetime_BG.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Dhaka is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time copenhagen'):
    tz_DK = pytz.timezone('Europe/Copenhagen')
    datetime_DK = datetime.now(tz_DK)
    msg = datetime_DK.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Dhaka is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)

  if message.content.startswith('!time copenhagen'):
    tz_DK = pytz.timezone('Europe/Copenhagen')
    datetime_DK = datetime.now(tz_DK)
    msg = datetime_DK.strftime("%Hh %Mm %Ss")
    embedVar = discord.Embed(title="The current time in Dhaka is", description=(msg), color=0x00ff00)
    await message.channel.send(embed=embedVar)




@client.event
async def on_guild_join(guild):
  general = find(lambda x: x.name == 'general',  guild.text_channels)
  if general and general.permissions_for(guild.me).send_messages:
    embedVar = discord.Embed(title="Earth Bot", description="I'm Earth Bot, and my only purpose is to make your server more fun, and being annoying", color=0x00ff00)
    embedVar.add_field(name="Welcome Bot", value="In case you want a DM bot that welcomes whoever joins your server, here's the link to connect it: \nhttps://bit.ly/3xsl9HQ", inline=False)
    embedVar.add_field(name="Help", value="For more information just type: *_!help_*", inline=False)
    embedVar.add_field(name="**Time Commands**", value="Do *!time commands* to see time commands you can do", inline=False)
    await general.send(embed=embedVar)


keep_alive.keep_alive()
client.run(os.getenv("token"))
