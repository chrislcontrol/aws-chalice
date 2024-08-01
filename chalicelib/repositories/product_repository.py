from typing import List, Optional
from chalicelib.entities.product import Product
from chalicelib.utils.exceptions import IntegrityError


class ProductRepository:
    _storage = {}

    def create(self, name: str, value: float, code: str) -> Product:
        if self._storage.get(code):
            raise IntegrityError()

        product = Product(code=code, name=name, value=value)

        self._storage[code] = product

        return product

    def find_by_code(self, code: str) -> Optional[Product]:
        return self._storage.get(code)

    def list_all(self) -> List[Product]:
        return self._storage.values()
