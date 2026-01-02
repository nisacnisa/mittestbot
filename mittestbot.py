from dotenv import load_dotenv
import discord
import os

#load environment variables from .env file
load_dotenv()

#setup intents
intents = discord.Intents.default()
intents.message_content = True #ensure that your bot cna read message content

client = discord.Client (intents=intents)

@clientevent
async def on_ready():
  print('We have logged in as {0.user}'. format (client)
        @clientevent
        async def on_message (message):
          if message.author == clientuser:
            return
        if message.content.startswith('$hello')
await message.channel.send('hello!')
client.run(os.getenv('TOKEN'))

    
