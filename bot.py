#this is the code for the discord bot that replies with pong when reads the message ping, trial bot using python

import discord
import os
import subprocess

intents = discord.Intents.default()
intents.message_content = True

Client = discord.Client(intents=intents)

OWNER_ID = # your Discord user ID

@Client.event
async def on_ready():
    print(f'logged in as {Client.user}')

@Client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == Client.user:
        return

    # Normal command (works for everyone)
    if message.content == "ping":
        await message.channel.send("pong")

    # Admin-only shutdown command
    if message.author.id == OWNER_ID and message.content == "!shutdown":
        await message.channel.send("Shutting down the server...")
        subprocess.run(["sudo", "/sbin/shutdown", "now"])

token = os.getenv("DISCORD_TOKEN")
Client.run(token)
