import time

import discord
from discord.ext import commands

from config import LOGGER
from utils.database import get_db
from utils.database.dao.guilds import GuildsDao


class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = next(get_db())

    @commands.Cog.listener()
    async def on_message(self, ctx: discord.Message):
        """Handle incoming messages."""
        if ctx.author.bot:
            return
        guild_dao = GuildsDao(self.db)
        guild = guild_dao.get_guild(ctx.guild.id)
        if guild is None:
            return

        if guild.channel_id != ctx.channel.id:
            return
        current_time = int(time.time())


def setup(bot):
    """Setup the event handler."""
    bot.add_cog(EventHandler(bot))
    LOGGER.info("Event handler loaded")
