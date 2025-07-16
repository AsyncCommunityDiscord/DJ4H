import discord
from discord.commands import slash_command
from discord.ext import commands

from config import LOGGER
from utils.database.dao.users import UserDao


def get_medal_emoji(position: int) -> str:
    """Get the medal emoji based on the user's position."""
    match position:
        case 1:
            return "🥇"
        case 2:
            return "🥈"
        case 3:
            return "🥉"
        case _:
            return f"#{position}"


class Game(commands.Cog):
    """Game commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def leaderboard(self, ctx) -> None:
        """Start the game."""
        if not ctx.guild:
            return

        user_dao = UserDao()
        leaderboard = user_dao.get_leaderboard(ctx.guild.id, 10)

        if not leaderboard:
            await ctx.respond("No users found in the leaderboard.")
            return

        leaderboard_text = "\n".join(
            f"{get_medal_emoji(i + 1)} <@{user.user_id}> - {user.score}"
            for i, user in enumerate(leaderboard)
        )
        embed = discord.Embed(
            title="Leaderboard",
            color=discord.Color.green(),
            description=leaderboard_text,
        )

        await ctx.respond(embed=embed)

    @slash_command()
    async def score(self, ctx) -> None:
        """Check your score."""
        if not ctx.guild:
            return

        user_dao = UserDao()
        user = user_dao.get_user(ctx.author.id, ctx.guild.id)

        if user is None:
            await ctx.respond("You have no score in this guild.")
            return

        await ctx.respond(f"Your score: {user.score}")


def setup(bot: commands.Bot) -> None:
    """Load the Game cog."""
    bot.add_cog(Game(bot))
    LOGGER.info("Game cog loaded successfully.")
