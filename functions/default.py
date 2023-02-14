from datetime import datetime
from logging import getLogger

from discord import ClientUser, Embed
from discord.commands import ApplicationContext
from discord.ext.commands import Cog

from classes import Bot
from config import COLOR
from constants import VERSION
from utils import slash_command

logger = getLogger(__name__)


class Default(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @slash_command(name="핑", description="봇의 핑을 전송합니다.")
    async def ping(self, ctx: ApplicationContext):
        embed = Embed(title=":ping_pong: 퐁!", color=COLOR)
        embed.add_field(
            name="discord API Ping: ", value=f"{round(self.bot.latency * 1000)} ms"
        )
        await ctx.respond(embed=embed)

    @slash_command(name="봇", description="봇의 정보를 전송합니다.")
    async def info(self, ctx: ApplicationContext):
        now = datetime.now()
        delta = now - self.bot.start_time
        embed = Embed(title="봇 정보", color=COLOR)
        if isinstance(self.bot.user, ClientUser):
            me = self.bot.user
        else:
            raise RuntimeError("Bot is not ready")
        embed.set_thumbnail(url=me.display_avatar.url)
        embed.add_field(name="봇 이름", value=f"**{me.name}** ({str(me)})", inline=False)
        embed.add_field(
            name="업타임",
            value=f"{delta.days} 일 {delta.seconds//3600} 시간 {(delta.seconds//60)%60} 분 {delta.seconds} 초",
            inline=False,
        )
        embed.add_field(name="봇 ID", value=str(me.id), inline=False)
        embed.add_field(
            name="세션 ID", value=f"||{str(self.bot.session)}||", inline=False
        )
        embed.add_field(name="버전", value=str(VERSION), inline=False)
        await ctx.respond(embed=embed)


def setup(bot: Bot):
    logger.info("Loaded")
    bot.add_cog(Default(bot))
