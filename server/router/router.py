from util.constants.misc import *
from .path import *
from .routes import routes

def route(request):
    method = request.method
    validate_path(request.target)
    path = get_filesystem_path(request.target)
    if method in STATIC_METHODS:
        routes[method](request)
    elif method in ACTION_METHODS:
        routes[path](request)