from fastapi.testclient import TestClient

def test_app():
    from app.main import app
    assert TestClient(app)