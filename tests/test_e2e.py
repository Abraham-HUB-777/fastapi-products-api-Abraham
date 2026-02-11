import requests


BASE_URL = "http://127.0.0.1:8000"


def test_create_and_low_stock():
    product = {
        "nombre": "Test",
        "precio": 50.0,
        "categoria": "tech",
        "stock": 3
    }

    r = requests.post(f"{BASE_URL}/products", json=product)
    assert r.status_code == 200

    r = requests.get(f"{BASE_URL}/products/low-stock?threshold=5")
    assert r.status_code == 200

    data = r.json()
    assert len(data) >= 1
    assert data[0]["nombre"] == "Test"
