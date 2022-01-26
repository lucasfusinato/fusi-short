from typing import Union
import os

database_type = os.environ.get('DATABASE_TYPE')

if database_type == 'memory':
    from .memory_db import MemoryDb
    database_instance = MemoryDb()
elif database_type == 'redis':
    from .redis_db import RedisDb
    database_instance = RedisDb(
        host=os.environ.get('DATABASE_HOST'),
        port=os.environ.get('DATABASE_PORT')
    )
else:
    raise AssertionError(f'Not supported db type "{database_type}"')

def is_short_url_exists(alias: str) -> bool:
    return database_instance.is_short_url_exists(alias=alias)

def set_short_url(alias: str, link: str) -> None:
    database_instance.set_short_url(alias=alias, link=link)

def get_short_url_link(alias: str) -> Union[str, None]:
    return database_instance.get_short_url_link(alias=alias)