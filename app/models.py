from pydantic import BaseModel


class Product(BaseModel):
    nombre: str
    precio: float
    categoria: str
    stock: int
