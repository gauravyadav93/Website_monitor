import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_site():
    response = client.post("/sites", json={"url": "https://example.com"})
    assert response.status_code == 200
    assert response.json()["url"] == "https://example.com"

def test_delete_site():
    response = client.delete("/sites/1")
    assert response.status_code == 