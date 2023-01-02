from discord.commands import SlashCommand, application_command # noqa

from config import TEST_GUILD_ID


def slash_command(**kwargs):
    if TEST_GUILD_ID is not None:
        kwargs["guild_ids"] = [TEST_GUILD_ID]

    return application_command(cls=SlashCommand, **kwargs)
