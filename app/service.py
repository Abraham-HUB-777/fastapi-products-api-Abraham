from typing import List
from .models import Product


class ProductService:
    def __init__(self):
        self._products: List[Product] = []

    def add_product(self, product: Product) -> None:
        self._products.append(product)

    def get_all(self) -> List[Product]:
        return self._products

    def low_stock(self, threshold: int) -> List[Product]:
        return [p for p in self._products if p.stock < threshold]
