import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.default()
# intents.message_content = True
# bot = discord.Client(intents=intents)
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # S

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    await bot.process_commands(message)

@bot.command()
async def test(ctx):
    # print(arg)
    await ctx.send("This is a button!", view=MyView()) # Send a message with our View class that contains the button

@bot.listen("on_button_click")
async def on_button_click(interaction):
    if interaction.component.custom_id == "option1":
        await interaction.respond(content="You chose Option 1!")
    elif interaction.component.custom_id == "option2":
        await interaction.respond(content="You chose Option 2!")


bot.run(TOKEN)