from chalice import Chalice
from chalice.app import Response
from chalicelib.routers.product_router import product_router
from chalicelib.utils.exceptions import HttpError

app = Chalice(app_name='product-service')
app.log.setLevel("DEBUG")
app.register_blueprint(product_router, url_prefix='/api/v1')


@app.route('/ping')
def index():
    return {'result': 'pong'}


@app.middleware('http')
def handle_validation_error_middleware(event, get_response):
    try:
        return get_response(event)
    except HttpError as exc:
        return Response(body=exc.get_detail(), status_code=exc.status)


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
