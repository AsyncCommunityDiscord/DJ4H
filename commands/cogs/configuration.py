import pathlib

import discord
from discord.commands import slash_command
from discord.ext import commands

from config import LOGGER
from utils.database.dao.guilds import GuildsDao
from utils.database.dao.users import UserDao


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
            raise ValueError("Invalid time format: Use 'm', 'h', or 'd'.")


class Configuration(commands.Cog):
    """Configuration commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @discord.default_permissions()
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
        try:
            converted_time = convert_time_to_seconds(delay)
        except ValueError as e:
            await ctx.respond(e)
            return

        if await GuildsDao.get_guild(ctx.guild.id) is None:
            await GuildsDao.add_guild(ctx.guild.id, channel.id, converted_time)
            await ctx.respond(
                f"Configuration setup: Channel: {channel.mention}, Delay: {delay}."
            )
            LOGGER.info(
                f"Guild {ctx.guild.id} configured with channel {channel.id} and delay {converted_time} seconds."
            )
            return

        await GuildsDao.update_guild(ctx.guild.id, channel.id, converted_time)
        await ctx.respond(
            f"Configuration updated: Channel: {channel.mention}, Delay: {delay}."
        )
        LOGGER.info(
            f"Guild {ctx.guild.id} updated with channel {channel.id} and delay {converted_time} seconds."
        )

    @slash_command()
    @discord.default_permissions()
    async def set(self, ctx, member: discord.Member, score: int):
        """Set a user's score."""
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server.")
            return

        user = await UserDao.get_user(member.id, ctx.guild.id)

        if user is None:
            await UserDao.add_user(member.id, ctx.guild.id, score)
            await ctx.respond(f"Set user {member.mention}'s score to {score}.")
            LOGGER.info(
                f"User {member.id} added to guild {ctx.guild.id} with score {score}."
            )
        else:
            await UserDao.update_user(member.id, ctx.guild.id, score)
            await ctx.respond(
                f"User {member.mention}'s score updated to {score}."
            )
            LOGGER.info(
                f"User {member.id} updated in guild {ctx.guild.id} with score {score}."
            )

    @slash_command()
    @discord.default_permissions()
    async def unset(self, ctx, member: discord.Member):
        """Unset a user's score."""
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server.")
            return

        user = await UserDao.get_user(member.id, ctx.guild.id)

        if user is None:
            await ctx.respond(
                f"User {member.mention} does not have a score set."
            )
            return

        await UserDao.delete_user(member.id, ctx.guild.id)
        await ctx.respond(f"Unset user {member.mention}'s score.")
        LOGGER.info(f"User {member.id} removed from guild {ctx.guild.id}.")

    @slash_command()
    @discord.default_permissions()
    async def dump_log(self, ctx):
        """Dump the bot's log."""
        if not ctx.guild:
            await ctx.respond("This command can only be used in a server.")
            return

        current_path = pathlib.Path(__file__).parent.resolve()
        log_file = pathlib.Path(f"{current_path}/../../logs/bot.log")
        if not log_file.exists():
            await ctx.respond("Log file does not exist.")
            return
        with open(log_file, "rb") as f:
            # send to private message
            await ctx.respond(
                "Here is the log file:",
                file=discord.File(f, "bot.log"),
                ephemeral=True,
            )


def setup(bot):
    """Load the Configuration cog."""
    bot.add_cog(Configuration(bot))
    LOGGER.info("Configuration cogs loaded.")
