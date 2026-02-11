from fastapi import FastAPI, Query
from typing import List
from .models import Product
from .service import ProductService

app = FastAPI()
service = ProductService()


@app.post("/products", response_model=Product)
def create_product(product: Product):
    service.add_product(product)
    return product


@app.get("/products/low-stock", response_model=List[Product])
def get_low_stock(threshold: int = Query(..., ge=0)):
    return service.low_stock(threshold)
