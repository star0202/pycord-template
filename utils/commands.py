from discord.commands import application_command, SlashCommand

from config import TEST_GUILD_ID


def slash_command(**kwargs):
    if TEST_GUILD_ID:
        kwargs["guild_ids"] = TEST_GUILD_ID

    return application_command(cls=SlashCommand, **kwargs)
