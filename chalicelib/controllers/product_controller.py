from chalice import Response

from chalicelib.use_cases.create_product import CreateProduct
from chalicelib.use_cases.list_products import ListProducts


class ProductController:
    def __init__(self,
                 create_product: CreateProduct,
                 list_products: ListProducts):
        self._create_product = create_product
        self._list_products = list_products

    def create_product(self, data: dict) -> Response:
        product = self._create_product.execute(
            code=data['code'],
            name=data['name'],
            value=data['value']
        )

        return Response(
            body={
                "code": product.code,
                "name": product.name,
                "value": product.value
            },
            status_code=201
        )

    def list_products(self) -> Response:
        products = self._list_products.execute()

        return Response(
            body=[
                {
                    "code": product.code,
                    "name": product.name,
                    "value": product.value
                } for product in products
            ],
            status_code=200
        )
