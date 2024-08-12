# bot.py
'''
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTI0ODM1MDMyOTg5Njk2NDIwNg.Gjixdh.J2lSDp70ov3rBqCcia_yH9ZaLPV-6doySFboQg')


import os
import discord
from app.chatgpt_ai.openai import chatgpt_response
from dotenv import load_dotenv

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.all()
# client = discord.Client(command_prefix="!", intents=intents)

class MyClient(discord.Client):
    
    # @client.event
    async def on_ready(self):
        print("We have logged in as {0.user}".format(client))
        
    # @client.event
    async def on_message(self, message):
        print(message.content)
        
        if message.author == self.user:
            return
        command, user_message=None, None

        # if message.content.startswith("hi"):
            # await message.channel.send("Hello World!")
        
        for text in ['/ai', '/bot', '/chatgpt']:
            if message.content.startswith(text):
                command=message.content.split(' ')[0]
                user_message=message.content.replace(text, '')
                print(command, user_message)
        
        
        #if command =='/ai':
        if message.content.startswith('/ai'):
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")
        
        
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')

            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)


client.run("MTI0ODM1MDMyOTg5Njk2NDIwNg.Gjixdh.J2lSDp70ov3rBqCcia_yH9ZaLPV-6doySFboQg")
'''

import os
import google.generativeai as genai
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=discord.Intents.default())

tree = discord.app_commands.CommandTree(client)

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

genai.configure(api_key="AIzaSyD3zhxgv4KmNIAQInSPU3sT7oNvzLuzAoA")
model = genai.GenerativeModel('gemini-pro',
	safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
	]
	)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


#
#@bot.command()
#async def echo(ctx: commands.Context, msg):
#    await ctx.send(msg)


# commands
@bot.command(name = "ai")
async def ai(ctx: commands.Context, *, prompt: str):
    response = model.generate_content(prompt)
    await ctx.reply(response.text)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)
    
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`")

'''
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id="MTI0ODM1MDMyOTg5Njk2NDIwNg.G1w_mn.aASkupceYuM0OXWHi6QIEOtFXtYU5iViGxz8do"))
    # print "ready" in the console when the bot is ready to work
    print("ready")
'''

'''
@tree.command(name="name", description="description")
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("command")
'''

bot.run('MTI0ODM1MDMyOTg5Njk2NDIwNg.G_6yPt.pzynZW5RjnsyLsLxE6Jy4yIAWTvXevNL0hqFFQ')
# client.run(TOKEN)

#response = model.generate_content("What is your name?")

#print(response.text)



'''
import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = 1260727059332857870

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

genai.configure(api_key="GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-pro',
    safety_settings=[
        {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
    ])

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}!")

    print(f"Bot ID: {bot.user.id}")
    try:
        guild = bot.get_guild(GUILD_ID)
        if guild:
            print(f"Bot is connected to guild: {guild.name} (ID: {guild.id})")
            commands = await guild.commands()
            print(f"Synced {len(commands)} commands in guild: {guild.name}")
        else:
            print(f"Guild with ID {GUILD_ID} not found or bot is not a member")
    except discord.errors.Forbidden as e:
        print(f"Failed to sync commands: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


@bot.command(name = "askai")
async def ai(ctx: commands.Context, *, prompt: str):
    response = model.generate_content(prompt)
    await ctx.reply(response.text)


@bot.command(name="ai", description="Generate AI response based on input")
#@app_commands.describe(prompt="The prompt to generate AI response for")
async def ai_command(interaction: discord.Interaction, prompt: str):
    response = model.generate_content(prompt)
    await interaction.response.send_message(f"AI response: {response.text}")


bot.run("MTI0ODM1MDMyOTg5Njk2NDIwNg.G_6yPt.pzynZW5RjnsyLsLxE6Jy4yIAWTvXevNL0hqFFQ")
'''