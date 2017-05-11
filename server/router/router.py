from .routes import routes
from util.constants.const_main import
from functools import partial
from util.path import validate_path
from server.actions.errors import do_error
from util.constants.response_codes import *


def get_request_handler_route(request):
    method = request.method
    path = request.target
    insert_aliases(request)

    is_valid_method = method in routes
    if not is_valid_method:
        return partial(do_error, METHOD_NOT_ALLOWED)

    handler = routes[method]

    is_method_with_action = isinstance(handler, dict)
    is_action_valid = path in handler if is_method_with_action else True
    is_path_valid = validate_path(path)

    if not is_path_valid and not is_action_valid:
        return partial(do_error, NOT_FOUND)

    return handler[path] if is_method_with_action else handler

def insert_aliases(request):
    if request.target in DEFAULT_PATH: #TODO switch to aliases
        request.target = DEFAULT_PATH[request.target]
    return request
