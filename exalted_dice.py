import discord
import random
import argparse

client = discord.Client()

def roll_dice(dice, add=0, double_on=[10]):
    values = []
    for die in range(dice):
        values.append(random.randrange(1, 11))
    values.sort()
    hits = len(list(filter(lambda x: x>=7, values)))
    hits += len(list(filter(lambda x: x in double_on, values)))
    hits += add
    if hits == 0 and 1 in values:
        return(f"{values} YOU DONE BOTCHED SON")
    return(f"{values} {hits} Successes")



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.name == channel:
        if message.content[0]=='!':
            input_string = message.content[1:]
            chunks = input_string.split(' ')
            dice = int(chunks[0])
            adds = 0
            doubles = [10]

            for chunk in chunks[1:]:
                if chunk[0] == 'a':
                    add = int(chunk[1:]) 
                    adds += add
                elif chunk[0] == 'd':
                    for digit in chunk[1:]:
                       doubles.append(int(digit))
                elif chunk[0] == 'r':
                    doubles = []

            results = roll_dice(dice, add=adds, double_on=doubles)
            await message.channel.send(results)


        if message.content.startswith('Hello'):
            await message.channel.send('I LIVE!')

parser = argparse.ArgumentParser()
parser.add_argument('--token', help='The Token For Your Bot To Use To Authenticate')
parser.add_argument('--roll_channel', help='The Channel the Bot Will Listen to Commands On')
parser.set_defaults(roll_channel='dice-rolling')
args = parser.parse_args()
token = args.token

global channel
channel = args.roll_channel

client.run(token)
