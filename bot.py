import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(f'{client.user} has connected to {guild.name}(id: {guild.id})!')
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.author.id == 431491910138462208 or message.author.id == 854207237441978408:
        embed = discord.Embed(title="HII DOGIEEEEEEE", color=0x00ff00)
        embed.set_image(url="https://media1.tenor.com/images/d9e1b251c03c939eea6b05ffec9cbda3/tenor.gif?itemid=11082453")
        await message.channel.send(embed=embed)
    elif "cheep" in message.content:
        embed = discord.Embed()
        embed.set_image(url="https://media1.tenor.com/images/e9c199654b91f8c0702b6fda7c59b072/tenor.gif?itemid=11550365")
        await message.channel.send(embed=embed)

client.run(TOKEN)
