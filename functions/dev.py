from json import loads
from logging import getLogger
from os import getenv
from traceback import format_exc

from aiosqlite import Error
from discord import ApplicationContext, Embed, Option
from discord.ext.commands import Cog

from classes import Bot
from config import BAD, COLOR
from utils import slash_command

logger = getLogger(__name__)
DEV_GUILD_ID = loads(getenv("DEV_GUILD_ID"))


class Dev(Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def stop(self, ctx: ApplicationContext):
        await ctx.respond("stopping..", ephemeral=True)
        await self.bot.close()

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def load_ext(self, ctx: ApplicationContext, ext_name: Option(str)):
        self.bot.load_extension(f"functions.{ext_name}")
        await ctx.respond(f"{ext_name}.py loaded", ephemeral=True)

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def unload_ext(self, ctx: ApplicationContext, ext_name: Option(str)):
        self.bot.unload_extension(f"functions.{ext_name}")
        await ctx.respond(f"{ext_name}.py loaded", ephemeral=True)

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def reload_ext(self, ctx: ApplicationContext, ext_name: Option(str)):
        self.bot.unload_extension(f"functions.{ext_name}")
        self.bot.load_extension(f"functions.{ext_name}")
        await ctx.respond(f"{ext_name}.py reloaded", ephemeral=True)

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def sql(self, ctx: ApplicationContext, sql: Option(str)):
        try:
            result = await self.bot.db.execute(sql)
            embed = Embed(title="Executed!", color=COLOR)
            embed.add_field(name="Script", value=f"```sql\n{sql}```")
            embed.add_field(name="Result", value=f"```py\n{result}```")
        except Error:
            embed = Embed(title="SQL Error", color=BAD)
            embed.add_field(name="Script", value=f"```sql\n{sql}```")
            embed.add_field(name="Error", value=f"```py\n{format_exc().splitlines()[-1]}```")
        await ctx.respond(embed=embed, ephemeral=True)

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def encrypt(self, ctx: ApplicationContext, content: Option(str)):
        embed = Embed(title="Encrypted!", color=COLOR)
        embed.add_field(name="Content", value=f"```{content}```")
        embed.add_field(name="Result", value=f"```{await self.bot.crypt.encrypt(content)}```")
        await ctx.respond(embed=embed, ephemeral=True)

    @slash_command(guild_ids=DEV_GUILD_ID)
    async def decrypt(self, ctx: ApplicationContext, content: Option(str)):
        embed = Embed(title="Decrypted!", color=COLOR)
        embed.add_field(name="Content", value=f"```{content}```")
        embed.add_field(name="Result", value=f"```{await self.bot.crypt.decrypt(content)}```")
        await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(Dev(bot))
