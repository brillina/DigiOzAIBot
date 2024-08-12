import os
import google.generativeai as genai
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands
load_dotenv()

# TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.default())

tree = discord.app_commands.CommandTree(client)

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
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

# Discord bot login
@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Gemini AI command
@bot.command(name = "ai")
async def ai(ctx: commands.Context, *, prompt: str):
    response = model.generate_content(prompt)
    await ctx.reply(response.text)

# Placeholder custom commands
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)
    
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`")

bot.run(os.environ.get("DISCORD_TOKEN"))