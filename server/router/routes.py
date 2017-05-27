from util.constants.const_main import *

from server.actions.publication import do_publish, do_delete
from server.actions.registration import do_register
from server.actions.get_pages import get_index, get_publication, get_profile, get_static, get_edit_post
from server.actions.head_pages import head_index, head_publication, head_profile, head_static
from server.actions.auth import do_auth, do_logout


routes = {
    GET: {
        INDEX: get_index,
        PUBLICATION: get_publication,
        USER_PAGE: get_profile,
        STATIC: get_static
    },
    HEAD: {
        INDEX: head_index,
        PUBLICATION: head_publication,
        USER_PAGE: head_profile,
        STATIC: head_static,
        EDIT_POST: get_edit_post
    },
    # OPTIONS: do_options,
    POST: {
        REGISTER: do_register,
        AUTH: do_auth,
        PUBLISH: do_publish,
        LOGOUT: do_logout,
        DELETE_POST: do_delete
    },

    PUT: {
        PUBLISH: do_publish
    },

    PATCH: {
        PUBLISH: do_publish
    },

    DELETE: {
        #
    }
}