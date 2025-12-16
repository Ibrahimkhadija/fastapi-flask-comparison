import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Flask" in response.data

def test_get_all_jokes(client):
    response = client.get("/jokes")
    assert response.status_code == 200
    assert len(response.json) == 5

def test_get_joke_by_id(client):
    response = client.get("/jokes/1")
    assert response.status_code == 200
    assert response.json["id"] == 1

def test_joke_not_found(client):
    response = client.get("/jokes/999")
    assert response.status_code == 404

def test_random_joke(client):
    response = client.get("/jokes/random")
    assert response.status_code == 200
    assert "joke" in response.json

def test_filter_by_category(client):
    response = client.get("/jokes?category=science")
    assert response.status_code == 200
    assert all(j["category"] == "science" for j in response.json)