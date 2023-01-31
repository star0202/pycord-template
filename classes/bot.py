from logging import getLogger
from os import getenv, listdir
from time import time
from traceback import format_exc, format_exception
from uuid import uuid4

from discord import ApplicationContext, DiscordException, Embed, ExtensionFailed, Game, Status
from discord.ext import commands
from discord.ext.commands import Context

from config import BAD, STATUS
from constants import OPTION_TYPES, DATABASE_INIT
from utils import setup_logging
from .crypt import AESCipher
from .database import Database


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(help_command=None)
        setup_logging()
        self.logger = getLogger(__name__)
        self.start_time = time()
        self.session = uuid4()
        self.crypt = AESCipher(getenv("TOKEN"))
        self.db = Database
        for filename in listdir("functions"):
            if filename.endswith(".py"):
                self.load_cog(f"functions.{filename[:-3]}")
        self.logger.info(f"{len(self.extensions)} extensions are completely loaded")

    def load_cog(self, cog: str):
        result = self.load_extension(cog, store=True)[cog]
        try:
            if isinstance(result, ExtensionFailed):
                self.logger.error("".join(format_exception(result)))
        except Exception as e:
            self.logger.error(e)

    def run(self):
        super().run(getenv("TOKEN"))

    async def on_ready(self):
        self.db = await self.db.create(getenv("DATABASE"), self.logger)
        for table in DATABASE_INIT:
            column_list = ""
            for column in table["columns"]:
                column_list += f"{column} {table['columns'][column]}, "
            await self.db.execute(f"CREATE TABLE IF NOT EXISTS {table['name']} ({column_list[:-2]})")
        self.logger.info(f"Logged in as {self.user.name}")
        self.logger.info(f"Session ID: {self.session}")
        await self.change_presence(
            status=Status.online,
            activity=Game(STATUS)
        )
        await self.wait_until_ready()

    async def on_command_error(self, ctx: ApplicationContext | Context, error: DiscordException):
        if hasattr(ctx.command, "on_error"):
            return
        text = "".join(format_exception(error))
        self.logger.error(text)
        await ctx.send(
            embed=Embed(
                title="오류 발생",
                description="개발자에게 문의 바랍니다.",
                color=BAD
            )
        )

    async def on_error(self, event, *args, **kwargs):
        if args[0]:
            await args[0].channel.send(
                embed=Embed(
                    title="오류 발생",
                    description="개발자에게 문의 바랍니다.",
                    color=BAD
                )
            )
        self.logger.error(format_exc())

    async def on_application_command(self, ctx: ApplicationContext):
        args = ""
        if ctx.selected_options:
            for option in ctx.selected_options:
                args += f"[Name: {option['name']}, Value: {option['value']}, Type: {OPTION_TYPES[option['type']]}] "
            args = args[:-1]
        guild = f"{ctx.guild}({ctx.guild.id})" if ctx.guild else "DM"
        self.logger.info(f"{ctx.user}({ctx.user.id}) in {guild}: /{ctx.command.name} {args}")
