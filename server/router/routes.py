from util.constants.const_main import *
from server.actions.actions import *

routes = {
    GET: do_get,
    HEAD: do_head,
    OPTIONS: do_options,
    POST: do_post,
    PUT: do_put,
    PATCH: do_patch
}