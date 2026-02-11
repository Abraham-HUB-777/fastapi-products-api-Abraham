# tests/test_e2e.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_low_stock():
    product = {
        "nombre": "Test",
        "precio": 50.0,
        "categoria": "tech",
        "stock": 3
    }
    response = client.post("/products", json=product)
    assert response.status_code == 200
