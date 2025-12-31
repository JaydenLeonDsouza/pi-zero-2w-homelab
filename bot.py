#this is the code for the discord bot that replies with pong when reads the message ping, trial bot

import discord

intents = discord.Intents.default()
intents.message_content = True

Client = discord.Client(intents=intents)

@Client.event
async def on_ready():
        print(f'logged in as {Client.user}')

@Client.event
async def on_message(message):
        if message.author == Client.user:
                return

        if message.content == "ping":
                await message.channel.send("pong")

import os

token = os.getenv("DISCORD_TOKEN")
Client.run(token)
