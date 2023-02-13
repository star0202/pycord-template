from datetime import datetime
from json import loads
from os import getenv
from time import mktime
from typing import Optional, Type, Any

from discord import Embed, SelectOption
from pytz import timezone


def get_time() -> datetime:
    return datetime.now(timezone("Asia/Seoul"))


def datetime_to_unix(n: datetime) -> int:
    return int(mktime(n.timetuple()))


def help_embed_maker(raw: dict[str, str], color: int) -> list[Embed]:
    obj_list: list[Embed] = []
    for title in raw:
        obj_list.append(Embed(title=title, description=raw[title], color=color))
    return obj_list


def help_select_maker(raw: dict[str, str]) -> list[SelectOption]:
    obj_list: list[SelectOption] = []
    for title in raw:
        obj_list.append(SelectOption(label=title, description=raw[title]))
    return obj_list


def load_env(
    name: str, return_type: Type = str, required: Optional[bool] = True
) -> Any:
    data = getenv(name)
    if isinstance(data, str):
        if return_type is str:
            return data
        if return_type is int:
            return int(data)
        if return_type is list:
            return loads(data)
    else:
        if required:
            raise RuntimeError(f"Environment variable {name} is not set")
        return None
