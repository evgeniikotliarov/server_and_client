from util.path import *
from .routes import routes

def get_request_handler_route(request):
    method = request.method
    validate_path(request.target)
    return routes[method]