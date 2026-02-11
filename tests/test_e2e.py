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

    # Crear producto
    response = client.post("/products", json=product)
    assert response.status_code == 200
    data = response.json()
    
    # Verificar que el producto creado tiene los mismos datos
    assert data["nombre"] == product["nombre"]
    assert data["precio"] == product["precio"]
    assert data["categoria"] == product["categoria"]
    assert data["stock"] == product["stock"]

    # Comprobar stock bajo
    LOW_STOCK_THRESHOLD = 5
    assert data["stock"] < LOW_STOCK_THRESHOLD
