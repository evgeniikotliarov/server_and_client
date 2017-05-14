from util.constants.const_main import *
from server.actions.actions import *
from server.actions.publication import do_publish
from server.actions.registration import do_register
from server.actions.auth import do_auth


routes = {
    GET: do_get,
    HEAD: do_head,
    OPTIONS: do_options,

    POST: {
        REGISTER: do_register,
        AUTH: do_auth,
        PUBLISH: do_publish
    },
    PUT: {
        PUBLISH: do_publish
    },
    PATCH: {
        PUBLISH: do_publish()
    }
}