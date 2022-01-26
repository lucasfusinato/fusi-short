from typing import Union

class RedisDb(object):
    def __init__(self, host: str, port: str):
        import redis
        self.__db = redis.Redis(host=host, port=port)

    def is_short_url_exists(self, alias: str) -> bool:
        return self.__db.exists(alias)

    def set_short_url(self, alias: str, link: str) -> None:
        self.__db.set(alias, link)

    def get_short_url_link(self, alias: str) -> Union[str, None]:
        return self.__db.get(alias)
