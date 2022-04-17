import discord
import ffmpeg
import configparser

config = configparser.ConfigParser()

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for attachment in message.attachments:
        if attachment.content_type == "video/webm":
            filename = attachment.filename.split(".")[0]
            ffmpeg.input(attachment.url)
            converted = ffmpeg.output("{0}.mp4".format(filename))

