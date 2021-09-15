import os
import math
import discord

token = os.environ['TOKEN']

def run():

    client = discord.Client() 
    @client.event
    async def on_redy(self):
        print(f'{self.user} has connected to Discord!')
    client.run (token)
    print ("hello wolrd")