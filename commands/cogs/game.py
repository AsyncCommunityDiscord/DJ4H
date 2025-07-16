from discord.commands import slash_command
from discord.ext import commands

from config import LOGGER
from utils.database.dao.users import UserDao


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
            f"#{i + 1}. <@{user.user_id}> - {user.score}"
            for i, user in enumerate(leaderboard)
        )
        await ctx.respond(f"**Leaderboard:**\n{leaderboard_text}")


def setup(bot: commands.Bot) -> None:
    """Load the Game cog."""
    bot.add_cog(Game(bot))
    LOGGER.info("Game cog loaded successfully.")
