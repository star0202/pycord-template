from datetime import datetime
from time import mktime
from typing import List, Dict, Union, Optional

from discord import Embed, SelectOption
from pytz import timezone


def get_time() -> datetime:
    return datetime.now(timezone("Asia/Seoul"))


def datetime_to_unix(n: datetime) -> int:
    return int(mktime(n.timetuple()))


def help_maker(raw: Dict, color: int, is_embed: Optional[bool] = True) -> List[Union[Embed, SelectOption]]:
    embed_list = []
    for title in raw:
        embed_list.append(
            Embed(
                title=title,
                description=raw[title],
                color=color
            )
            if is_embed else
            SelectOption(
                label=title,
                description=raw[title]
            )
        )
    return embed_list
