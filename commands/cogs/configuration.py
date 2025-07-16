import discord
from discord.commands import slash_command
from discord.ext import commands

from config import LOGGER
from utils.database.dao.guilds import GuildsDao


def convert_time_to_seconds(time_str: str) -> int:
    """Convert a time string (e.g., '5m', '4h', '3d') to seconds."""
    match time_str.lower()[-1]:
        case "s":
            return int(time_str[:-1])
        case "m":
            return int(time_str[:-1]) * 60
        case "h":
            return int(time_str[:-1]) * 60 * 60
        case "d":
            return int(time_str[:-1]) * 24 * 60 * 60
        case _:
            raise ValueError("Invalid time format. Use 'm', 'h', or 'd'.")


class Configuration(commands.Cog):
    """Configuration commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def config(
        self,
        ctx,
        channel: discord.TextChannel,
        delay: discord.Option(
            str, description="Delay between messages. Ex: 30s, 5m, 4h, 3d"
        ),
    ) -> None:
        """Config game channel."""

        if not ctx.guild:
            await ctx.respond("This command can only be used in a server.")
            return

        converted_time = convert_time_to_seconds(delay)
        guilds_dao = GuildsDao()

        if guilds_dao.get_guild(ctx.guild.id) is None:
            guilds_dao.add_guild(ctx.guild.id, channel.id, converted_time)
            await ctx.respond(
                f"Configuration setup: Channel: {channel.mention}, Delay: {delay}."
            )
            LOGGER.info(
                f"Guild {ctx.guild.id} configured with channel {channel.id} and delay {converted_time} seconds."
            )
            return

        guilds_dao.update_guild(ctx.guild.id, channel.id, converted_time)
        await ctx.respond(
            f"Configuration updated: Channel: {channel.mention}, Delay: {delay}."
        )
        LOGGER.info(
            f"Guild {ctx.guild.id} updated with channel {channel.id} and delay {converted_time} seconds."
        )


def setup(bot):
    """Load the Configuration cog."""
    bot.add_cog(Configuration(bot))
    LOGGER.info("Configuration cogs loaded.")
