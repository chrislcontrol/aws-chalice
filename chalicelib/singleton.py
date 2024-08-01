from chalicelib.controllers.product_controller import ProductController
from chalicelib.repositories.product_repository import ProductRepository
from chalicelib.use_cases.create_product import CreateProduct
from chalicelib.use_cases.list_products import ListProducts


class _STRepo:
    product_repository = ProductRepository()


class _STUseCases:
    create_product = CreateProduct(
        product_repository=_STRepo.product_repository)
    list_products = ListProducts(product_repository=_STRepo.product_repository)


class _STControllers:
    product_controller = ProductController(create_product=_STUseCases.create_product,
                                           list_products=_STUseCases.list_products)


class Singleton:
    @classmethod
    def get_product_controller(cls) -> ProductController:
        return _STControllers.product_controller
