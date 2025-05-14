import discord
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv
import datetime

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)


CHANNEL_ID = 769447115285463040  
START_HOUR = 9
END_HOUR = 2


def is_within_allowed_hours():
    now = datetime.datetime.now().time()
    hour = now.hour
    if START_HOUR < END_HOUR:
        return START_HOUR <= hour < END_HOUR
    else:
        return hour >= START_HOUR or hour < END_HOUR

@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user}')
    reminder_loop.start()

@tasks.loop(hours=2)
async def reminder_loop():
    if is_within_allowed_hours():
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            await channel.send("<@&769446741866971148> getcho money twin!💰💸 ")

bot.run(TOKEN)
