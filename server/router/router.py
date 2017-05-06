from .routes import method_routes, action_routes
from util.constants.const_main import DEFAULT_PATHS


def get_request_handler_route(request):
    method = request.method
    if request.target in DEFAULT_PATHS:
        request.target = DEFAULT_PATHS[request.target]
    return method_routes[method]


def get_action_route(request):
    target = request.target
    return action_routes[target]