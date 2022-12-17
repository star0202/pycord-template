from logging import getLogger

import discord
from discord.commands import ApplicationContext
from discord.ext import commands

from config import COLOR
from constants import HELP_SELECT_RAW, HELP_EMBED_RAW
from utils.commands import slash_command
from utils.utils import help_maker

logger = getLogger(__name__)

help_list = list(HELP_SELECT_RAW.keys())
help_select = help_maker(HELP_SELECT_RAW, COLOR, False)
help_embed = help_maker(HELP_EMBED_RAW, COLOR)


class HelpMenu(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    @discord.ui.select(placeholder="명령어를 선택하세요", options=help_select)
    async def callback(self, select, interaction: discord.Interaction):
        await interaction.response.edit_message(embed=help_embed[help_list.index(select.values[0])], view=self)


class Help(commands.Cog):
    @slash_command(name="도움말", description="도움말을 출력합니다.")
    async def help(self, ctx: ApplicationContext):
        embed = discord.Embed(title="도움말", description="메뉴에서 원하는 명령어를 선택하세요.", color=COLOR)
        embed.add_field(name="참고사항", value="`[입력값]` : 필수 입력값  |  `(입력값)` : 선택 입력값")
        await ctx.respond(embed=embed, view=HelpMenu())


def setup(bot):
    logger.info("Loaded")
    bot.add_cog(Help(bot))


def teardown():
    logger.info("Unloaded")
