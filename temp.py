import os

import discord
import random
from dotenv import load_dotenv
import requests



base_url = "http://numbersapi.com"


TOKEN = "OTY4MDk4NjQ5MjUyOTYyMzE1.YmZ6IA.xtGekYNcS-I17wQT9QEDdqCpe9c"

client = discord.Client()

server_name = "YISS Community"

def to_int(x: str):
    try:
        return int(x)
    except:
        return None
def int_from_roman_numeral(x: str):
    """
    Convert x from roman numeral to int
    Return None if x is not a valid roman numeral
    """
    thousands = ['M', 'MM', 'MMM']
    hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

    x = x.upper().strip()
    if not x:
        return None

    total = 0
    num = None
    value = None

    for i in range(len(thousands)):
        n = thousands[i]
        v = 1000 * (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]

    num = None
    value = None

    for i in range(len(hundreds)):
        n = hundreds[i]
        v = 100 * (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]

    num = None
    value = None

    for i in range(len(tens)):
        n = tens[i]
        v = 10 * (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass
    if num is not None:
        total += value
        x = x[len(num):]

    num = None
    value = None

    for i in range(len(ones)):
        n = ones[i]
        v = (i + 1)
        try:
            if x.index(n) == 0:
                num = n
                value = v
        except:
            pass

    if num is not None:
        total += value
        x = x[len(num):]
    if len(x) != 0:
        return None
    return total

@client.event
async def on_ready():
    server = discord.utils.get(client.guilds, name=server_name)
    print("Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    num = to_int(message.content)
    num = int_from_roman_numeral(message.content) if num is None else num
    if num is None:
        return

    response = requests.get(f"{base_url}/{num}")
    await message.channel.send(response.text)

client.run(TOKEN)