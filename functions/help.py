from logging import getLogger

from discord import Embed
from discord.commands import ApplicationContext
from discord.ext import commands

from classes import Bot
from config import COLOR
from utils import slash_command
from views import HelpMenu

logger = getLogger(__name__)


class Help(commands.Cog):
    @slash_command(name="도움말", description="도움말을 출력합니다.")
    async def help(self, ctx: ApplicationContext):
        embed = Embed(title="도움말", description="메뉴에서 원하는 명령어를 선택하세요.", color=COLOR)
        embed.add_field(name="참고사항", value="`[입력값]` : 필수 입력값  |  `(입력값)` : 선택 입력값")
        await ctx.respond(embed=embed, view=HelpMenu())


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(Help(bot))
