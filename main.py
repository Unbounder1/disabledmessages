import discord
import re
intents = discord.Intents.default()
client = discord.Client(intents=intents)
print ("your forbidden messages are " + str(open('forbiddenmessages', 'r').read().splitlines()))
@client.event
async def on_message(message):
    if message.author.bot: return
    cantuse = open('forbiddenmessages', 'r').read().splitlines()
    for i in cantuse:
        if re.match(i, message.content, re.I) == None:
            continue
        else:
            await message.delete()
            await message.channel.send('DO NOT USE THAT LANGUAGE HERE')
            print (str(message.author) + " used " + str(i))
            return
        return
with open('config', "r") as config:

    clientid = config.readlines()

client.run(clientid[1])
