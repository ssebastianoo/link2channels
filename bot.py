import discord
import os

client = discord.Client()

@client.event
async def on_ready():

  print('Ready as', client.user)

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  guild1 = client.get_guild(1234)
  guild2 = client.get_guild(4321)

  channel1 = discord.utils.get(guild1.channels, name = 'channel1') 
  channel2 = discord.utils.get(guild2.channels, name = 'channel2')

  emb = discord.Embed(description = message.content, colour = message.author.colour)
  emb.set_author(name = message.author, icon_url = message.author.avatar_url)

  if message.guild == guild1:
    await channel2.send(embed = emb)
    return

  if message.guild == guild2:
    await channel1.send(embed = emb)
    return


client.run()
