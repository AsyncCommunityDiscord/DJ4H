import discord

from config import BOT_TOKEN, DEBUG_GUILD_ID, setup_logging
from utils.database.connection import Base, engine

setup_logging()

bot = discord.Bot(
    intents=discord.Intents.default(),
    help_command=None,  # Disable the default help command
    activity=discord.Game(name="Type /help for commands"),
    debug_guilds=[DEBUG_GUILD_ID] if DEBUG_GUILD_ID else None,
)


Base.metadata.create_all(engine)
bot.load_extensions("commands", recursive=True)
bot.run(BOT_TOKEN)
