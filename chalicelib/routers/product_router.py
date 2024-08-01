from chalice import Blueprint

from chalicelib.singleton import Singleton


product_router = Blueprint(__name__)
_controller = Singleton.get_product_controller()


@product_router.route(
    path="/products",
    methods=["POST"],
    cors=True,
    content_types=['application/json']
)
def create():
    request = product_router.current_request
    return _controller.create_product(request.json_body)


@product_router.route(
    path="/products",
    methods=["GET"],
    cors=True,
    content_types=['application/json']
)
def list_products():
    return _controller.list_products()
