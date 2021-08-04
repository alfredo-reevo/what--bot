# This bot automatically and instantaneously removes any message within the text channel "❓-what" that does not equate to "What?"
# Made for kenzie's discord server because I was bored

# Programmed by Alfie Reeves (jimmelton @ Github)

import discord

TOKEN = ""

client = discord.Client()

@client.event
async def on_ready():
    print("I am ready")

@client.event
async def on_message(msg):
    user_msg = str(msg.content)
    if msg.channel.name == "❓-what":
        if user_msg.strip() != "What?":
            await msg.delete()
        else:
            pass

@client.event
async def on_message_edit(before, after):
    if after.channel.name == "❓-what":
        if after.content != "What?":
            await after.delete()
            return


client.run(TOKEN)
