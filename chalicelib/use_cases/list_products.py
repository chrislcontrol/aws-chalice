from typing import List
from chalicelib.entities.product import Product
from chalicelib.repositories.product_repository import ProductRepository


class ListProducts:
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def execute(self) -> List[Product]:
        return self._product_repository.list_all()
