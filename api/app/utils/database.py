from typing import Union

short_urls = {}

def is_short_url_exists(alias: str) -> bool:
    return alias in short_urls

def set_short_url(alias: str, link: str) -> None:
    short_urls[alias] = link

def get_short_url_link(alias: str) -> Union[str, None]:
    if alias in short_urls:
        return short_urls[alias]
    return None
