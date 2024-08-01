from chalicelib.entities.product import Product
from chalicelib.repositories.product_repository import ProductRepository
from chalicelib.utils.exceptions import HttpError, IntegrityError


class CreateProduct:
    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def execute(self, name: str, code: str, value: float) -> Product:
        try:
            return self._product_repository.create(name=name, code=code, value=value)
        except IntegrityError as exc:
            raise HttpError("Product already exists", 409) from exc
