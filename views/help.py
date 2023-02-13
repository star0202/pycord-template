from discord import Interaction
from discord.ui import View, select

from config import COLOR
from constants import HELP_EMBED_RAW, HELP_SELECT_RAW
from utils import help_embed_maker, help_select_maker

help_list = list(HELP_SELECT_RAW.keys())
help_select = help_select_maker(HELP_SELECT_RAW)
help_embed = help_embed_maker(HELP_EMBED_RAW, COLOR)


class HelpMenu(View):
    def __init__(self):
        super().__init__(timeout=60)

    @select(placeholder="명령어를 선택하세요", options=help_select)
    async def callback(self, slt, interaction: Interaction):
        await interaction.response.edit_message(
            embed=help_embed[help_list.index(slt.values[0])], view=self
        )
