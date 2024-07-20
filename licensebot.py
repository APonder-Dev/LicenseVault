import discord
from discord.ext import commands
import sqlite3
import uuid
from datetime import datetime, timedelta
import os

# Loads the token from the .env file
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Initializes the bot
bot = commands.Bot(command_prefix="!")

# Connects to the SQLite database
conn = sqlite3.connect('licenses.db')
cursor = conn.cursor()

# Creates the licenses table
cursor.execute('''
CREATE TABLE IF NOT EXISTS licenses (
    user_id TEXT PRIMARY KEY,
    license_key TEXT,
    expiration_date TEXT
)
''')
conn.commit()

@bot.command(name='generate_license')
@commands.has_permissions(administrator=True)
async def generate_license(ctx, user: discord.User, duration_days: int):
    license_key = str(uuid.uuid4())
    expiration_date = datetime.now() + timedelta(days=duration_days)
    cursor.execute("INSERT OR REPLACE INTO licenses (user_id, license_key, expiration_date) VALUES (?, ?, ?)",
                   (str(user.id), license_key, expiration_date.strftime('%Y-%m-%d')))
    conn.commit()
    await ctx.send(f"Generated license key for {user.name}: {license_key} (expires on {expiration_date.strftime('%Y-%m-%d')})")

def validate_license(user_id):
    cursor.execute("SELECT expiration_date FROM licenses WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    if result:
        expiration_date = datetime.strptime(result[0], '%Y-%m-%d')
        if expiration_date > datetime.now():
            return True
    return False

@bot.command(name='check_license')
async def check_license(ctx):
    user_id = str(ctx.author.id)
    cursor.execute("SELECT license_key, expiration_date FROM licenses WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    if result:
        license_key, expiration_date = result
        expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
        if expiration_date > datetime.now():
            await ctx.send(f"Your license key: {license_key} (expires on {expiration_date.strftime('%Y-%m-%d')})")
        else:
            await ctx.send("Your license has expired.")
    else:
        await ctx.send("You do not have a license.")

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

bot.run(TOKEN)