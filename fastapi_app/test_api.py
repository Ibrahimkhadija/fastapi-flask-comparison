from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "FastAPI" in response.json()["message"]

def test_get_all_jokes():
    response = client.get("/jokes")
    assert response.status_code == 200
    assert len(response.json()) == 5

def test_get_joke_by_id():
    response = client.get("/jokes/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_joke_not_found():
    response = client.get("/jokes/999")
    assert response.status_code == 404

def test_random_joke():
    response = client.get("/jokes/random")
    assert response.status_code == 200
    assert "joke" in response.json()

def test_filter_by_category():
    response = client.get("/jokes?category=science")
    assert response.status_code == 200
    assert all(j["category"] == "science" for j in response.json())