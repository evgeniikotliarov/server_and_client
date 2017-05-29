from .routes import routes
from aliases import ALIASES
from functools import partial
from util.path import validate_path
from server.actions.error import do_not_found_error
from util.constants.response_codes import *
from util.constants.const_main import STATIC


def get_request_handler_route(request):
    insert_aliases(request)
    method, path = request.method, request.target

    is_valid_method = method in routes
    if not is_valid_method: return partial(do_not_found_error(), METHOD_NOT_ALLOWED)
    handler = routes[method]

    is_path_valid = validate_path(path)
    is_action_valid = path in handler

    if not (is_path_valid or is_action_valid):
        return partial(do_not_found_error(), NOT_FOUND)

    return handler[path] if is_action_valid else handler[STATIC]


def insert_aliases(request):
    if request.target in ALIASES:
        request.target = ALIASES[request.target]
    return request