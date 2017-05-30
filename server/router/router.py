from functools import partial
from .routes import routes
from aliases import ALIASES
from server.actions.error import do_not_found_error
from server.actions.get_pages import get_static
from server.actions.head_pages import head_static
from util.constants.response_codes import *
from util.constants.const_main import HEAD, GET
from util.path import is_valid_static


def get_route(request):
    insert_aliases(request)  # TODO move out to request transformer
    method, path = request.method, request.target
    for route in routes:
        if route.has_method(method) and route.has_path(path):
            return route.get_handler()

    if not is_valid_static(path): return partial(do_not_found_error, NOT_FOUND)
    elif method == GET: return get_static
    elif method == HEAD: return head_static
    else: return partial(do_not_found_error, METHOD_NOT_ALLOWED)


def insert_aliases(request):
    if request.target in ALIASES:
        request.target = ALIASES[request.target]
    return request