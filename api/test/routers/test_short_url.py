from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_post_short_url():
    response = client.post('/short-url', json={'link': 'www.google.com', 'alias': 'test_short_url'})
    assert response.status_code == 200
    assert response.json() == {'alias': 'test_short_url'}
    
def test_get_short_url():
    response = client.get('/short-url/test_short_url')
    assert response.status_code == 200
    assert response.json() == {'link': 'www.google.com'}