from typing import Union

class MemoryDb(object):
    def __init__(self):
        self.__short_urls = {}

    def is_short_url_exists(self, alias: str) -> bool:
        return alias in self.__short_urls

    def set_short_url(self, alias: str, link: str) -> None:
        self.__short_urls[alias] = link

    def get_short_url_link(self, alias: str) -> Union[str, None]:
        if alias in self.__short_urls:
            return self.__short_urls[alias]
        return None
