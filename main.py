import os
import alive
import discord
import encrypt
import asyncio
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import sys
import math
import base64
import random
import MATH

gyefgygrighziguyhrihgirughuirghurhughruhgurhguhioiisi = os.environ['TOKEN']

blah_x = "https://www.google.com/search?q=cat&hl=en&tbm=isch&sxsrf=AOaemvKntgeM7GsmwJ9E0tb3PbGLAMO5bw%3A1630995536230&source=hp&biw=&bih=&ei=UAQ3YZiHDKWp1sQP2pS1wA8"

token = "well done hacker \n but u frogot who made the bot"
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('sudo help'):
        await message.channel.send(
            '``` 1.sudo help \n 2.sudo do 5+5 \n 3.sudo reverse  \n 4.sudo encrypt base64 \n 5.sudo fetch body \n 6 sudo fetch head```'
        )
    if message.content.startswith('sudo do'):
        msg = message.content
        msg = msg[7:]
        x = eval(msg)
        await message.channel.send(str(x))

    if message.content.startswith('sudo reverse'):
        msg = message.content
        msg = msg[13:]
        msg = encrypt.reverse(msg)
        await message.channel.send(str(msg))
    if message.content.startswith('sudo encrypt '):
        msg = message.content
        msg = msg[12:]
        encodedBytes = base64.b64encode(msg.encode("utf-8"))
        msg = str(encodedBytes, "utf-8")
        await message.channel.send(msg)
        pass
    if message.content.startswith('sudo decrypt '):
        msg = message.content
        msg = msg[12:]
        base64_string = str(msg)

        msg = base64.b64decode(msg)
        msg = msg.decode("ascii")
        await message.channel.send(msg)
        pass
    if message.content.startswith('sudo ddos strike '):
        msg = message.content
        msg = msg[17:]
        msg = int(msg) + 1
        for i in range(msg):
            await message.channel.send("DDOS strike " + str(i) + " by " +
                                       str(message.author))

    if message.content.startswith('sudo ddos doomsday'):
        msg = message.content
        while True:
            await message.channel.send("DDOS strike " + "infinity" + " by " +
                                       str(message.author))
    if message.content.startswith('sudo is flask alive?'):

        html = urlopen("https://anti-spy.pr00tt0y.repl.co").read()
        await message.channel.send(str(html))
    if message.content.startswith('sudo fetch html'):
        msg = message.content
        msg = msg[16:]
        msg = str(msg)
        html = urlopen(msg).read()
        await message.channel.send(str(html))
    if message.content.startswith('sudo fetch head '):
        msg = message.content
        msg = msg[16:]
        msg = str(msg)
        msg = str(msg)
        url = msg
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        head = soup.find('head')
        head = "```html\n " + str(head) + "```"
        await message.channel.send(head)
    if message.content.startswith('sudo fetch body '):
        msg = message.content
        msg = msg[16:]
        msg = str(msg)
        msg = str(msg)
        url = msg
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        body = soup.find('body')

        body = "```html\n " + str(body) + "```"
        await message.channel.send(body)
    if message.content.startswith('sudo kill'):
        await message.channel.send("innah lillah")
        sys.exit()
    #==========================================================================================================

    #random_index = random.randint(0,len(images)-1)
    #await message.channel.send (images[int(random_index)])

    if message.content == ".":
        await message.channel.send(". no u")


@client.event
async def on_message_delete(message):
    msg = message.content

    await message.channel.send('`' + str(message.author) + '`' +
                               "has deleted : ")
    e = base64.b64encode(msg.encode("utf-8"))
    msg = str(e, "utf-8")

    await message.channel.send("    ```" + str(msg) + "```")


MATH.run()
alive.keep_alive()
client.run(gyefgygrighziguyhrihgirughuirghurhughruhgurhguhioiisi)
print("program finished")
