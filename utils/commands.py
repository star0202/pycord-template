from discord.commands import SlashCommand, application_command
from typing import Callable
from config import TEST_GUILD_ID


def apply_if_not_none(value, block: Callable):
    if value is not None:
        value = block(value)
    return value


def slash_command(**kwargs):
    if TEST_GUILD_ID is not None:
        kwargs["guild_ids"] = [TEST_GUILD_ID]

    return application_command(cls=SlashCommand, **kwargs)
