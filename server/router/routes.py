from util.constants.const_main import *

import server.actions.publication as publication
from server.actions.registration import do_register
from server.actions.head_pages import *
from server.actions.auth import do_auth, do_logout
from server.router.route import Route


routes = [
    Route(GET, INDEX, get_index),
    Route(GET, PUBLICATION_PAGE, get_publication),
    Route(GET, PROFILE_PAGE, get_profile),
    Route(GET, EDIT_POST_PAGE, get_edit_post),

    Route(HEAD, INDEX, head_index),
    Route(HEAD, PUBLICATION_PAGE, head_publication),
    Route(HEAD, PROFILE_PAGE, head_profile),
    Route(HEAD, EDIT_POST_PAGE, head_edit_post),

    Route(POST, REGISTER_ACTION_PAGE, do_register),
    Route(POST, AUTH_ACTION_PAGE, do_auth),
    Route(POST, LOGOUT_ACTION_PAGE, do_logout),
    Route([POST, PUT, PATCH], PUBLISH_ACTION_PAGE, publication.do_publish),
    Route([POST, DELETE], DELETE_POST_ACTION_PAGE, publication.do_delete),
    Route([POST, PATCH], EDIT_POST_ACTION_PAGE, publication.do_edit),
]
