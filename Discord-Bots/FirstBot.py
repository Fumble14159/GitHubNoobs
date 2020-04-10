import discord
import asyncio
import random
from discord.ext import commands


#client = discord.Client()
client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():                                   #Message that pops up in CMD when we run our bot
    print('Bot running as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('lmao'):
        await message.channel.send('LMAOKAI!')
    
    if message.content.startswith('$purge'): 
        await message.delete                        #Deletes the message if it starts with '$purge'
        await message.channel.send('Purged')
    await client.process_commands(message)          #Have to put this here for the command below to work

@client.command()                                  
async def clear(ctx, amount):                        #Delete an 'amount' of messages
   await ctx.channel.purge(limit=int(amount))    


        

client.run('Hidden because of safety!')