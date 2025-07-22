import json
import logging.config
import os
import pathlib

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

DEBUG_GUILD_ID = os.getenv("DEBUG_GUILD_ID", None)
if DEBUG_GUILD_ID is not None:
    try:
        DEBUG_GUILD_ID = int(DEBUG_GUILD_ID)
    except ValueError:
        raise ValueError(
            "DEBUG_GUILD_ID must be an integer representing a guild ID."
        )


DATABASE_PATH = os.getenv("DATABASE_PATH", "dj4h.db")


def setup_logging():

    current_path = pathlib.Path(__file__).parent.resolve()
    config_file = pathlib.Path(f"{current_path}/log_config.json")
    os.makedirs("logs", exist_ok=True)
    with open(config_file) as f_in:
        config = json.load(f_in)

    logging.config.dictConfig(config)


LOGGER = logging.getLogger("DJ4H")
