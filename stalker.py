import discord
from discord.ext.commands import Bot
from discord import DMChannel
TOKEN = "OTY4MDk4NjQ5MjUyOTYyMzE1.YmZ6IA.xtGekYNcS-I17wQT9QEDdqCpe9c"
client = Bot (command_prefix='!')
server_name = "YISS Community"
@client.event
async def on_ready():
    server = discord.utils.get(client.guilds, name=server_name)
    print("Ready")
@client.command(name='dmsend', pass_context=True)
async def dmsend(ctx):
    user = await client.fetch_user("832129319647051807")
    await DMChannel.send(user, "discord.gg/friends")
@client.event
async def on_message(message):
    channel = client.get_channel(972117023666626640)
    if message.guild is None and message.author != client.user:
        await channel.send(f"{message.author} sent {message.content}")
    await client.process_commands(message)

client.run(TOKEN)