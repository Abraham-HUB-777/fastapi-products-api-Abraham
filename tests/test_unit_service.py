from app.service import ProductService
from app.models import Product


def test_low_stock_returns_correct_products():
    service = ProductService()

    p1 = Product(nombre="A", precio=10.0, categoria="cat1", stock=5)
    p2 = Product(nombre="B", precio=20.0, categoria="cat2", stock=15)

    service.add_product(p1)
    service.add_product(p2)

    result = service.low_stock(10)

    assert len(result) == 1
    assert result[0].nombre == "A"
