# This bot automatically and instantaneously removes any message within the text channel "❓-what" that does not equate to "What?"
# Made for kenzie's discord server because I was bored

# Programmed by Alfie Reeves (jimmelton @ Github)

import discord

TOKEN = "ODcyNTIzMzIyNTQwMzIyODE2.YQrGqg.OY21owvCqj-ND3y9Vho4_5Zw2Dk"

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


client.run(TOKEN)