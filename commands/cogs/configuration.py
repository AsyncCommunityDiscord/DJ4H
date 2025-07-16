from discord.ext import commands

from config import LOGGER


class Configuration(commands.Cog):
    """Configuration commands for the bot."""

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    """Load the Configuration cog."""
    bot.add_cog(Configuration(bot))
    LOGGER.info("Configuration loaded.")
