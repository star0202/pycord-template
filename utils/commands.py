from discord.commands import SlashCommand, application_command

from utils import load_env

TEST_GUILD_ID = load_env("TEST_GUILD_ID", list, False)


def slash_command(**kwargs):
    if TEST_GUILD_ID:
        kwargs["guild_ids"] = TEST_GUILD_ID

    return application_command(cls=SlashCommand, **kwargs)
