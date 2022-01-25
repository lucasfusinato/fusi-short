
from api.app.utils import database

def test_set_short_url():
    database.set_short_url(alias='test_database', link='www.google.com')
    assert database.is_short_url_exists('test_database')

def test_is_short_url_exists():
    assert database.is_short_url_exists('test_database')
    assert not database.is_short_url_exists('empty')

def test_get_short_url_link():
    assert database.get_short_url_link('test_database') == 'www.google.com'