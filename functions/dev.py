from logging import getLogger

from discord import ApplicationContext, Option
from discord.ext import commands

from utils.commands import slash_command

logger = getLogger(__name__)


class Dev(commands.Cog, command_attrs={"hidden": True}):
    def __init__(self, bot):
        self.bot = bot
        self.jishaku = bot.get_cog("jishaku")

    @slash_command()
    async def stop(self, ctx: ApplicationContext):
        if await self.bot.is_owner(ctx.user):
            await ctx.respond("stopping..")
            await self.bot.close()

    @slash_command()
    async def load_ext(self, ctx: ApplicationContext, ext_name: Option(str)):
        if await self.bot.is_owner(ctx.user):
            self.bot.load_extension(f"functions.{ext_name}")
            await ctx.respond(f"{ext_name}.py loaded")

    @slash_command()
    async def unload_ext(self, ctx: ApplicationContext, ext_name: Option(str)):
        if await self.bot.is_owner(ctx.user):
            self.bot.unload_extension(f"functions.{ext_name}")
            await ctx.respond(f"{ext_name}.py loaded")

    @slash_command()
    async def reload_ext(self, ctx: ApplicationContext, ext_name: Option(str)):
        if await self.bot.is_owner(ctx.user):
            self.bot.unload_extension(f"functions.{ext_name}")
            self.bot.load_extension(f"functions.{ext_name}")
            await ctx.respond(f"{ext_name}.py reloaded")

    @slash_command()
    async def send_here(self, ctx: ApplicationContext, content: Option(str)):
        if await self.bot.is_owner(ctx.user):
            await ctx.send(content)
            delete_this = await ctx.respond("random respond")
            await delete_this.delete_original_response()


def setup(bot):
    logger.info("Loaded")
    bot.add_cog(Dev(bot))


def teardown():
    logger.info("Unloaded")
