from storage.sessions_dao_factory import SessionsDAOFactory
from storage.users_dao_factory import UsersDAOFactory

from paths import *
from server.form_encodings.decoder import decode_body
from util.constants.const_main import SESSION, SESSION_DEFAULT_AGE, IN_MEMORY
from util.redirect import do_redirect, wrong_credentials


def do_auth(request, response_builder):
    new_user = decode_body(request)
    username = new_user['user'].decode().strip()
    password = new_user['password'].decode().strip()
    valid_user = __validate_user(username, password)

    if valid_user:
        session = SessionsDAOFactory.get_storage(IN_MEMORY).create_session(username, SESSION_DEFAULT_AGE)
        response_builder.set_cookie(b"%s=%s; max-age=%d" %
                                    (SESSION, session.get_id().encode(), session.max_age, ))
        return do_redirect(INDEX_PAGE, response_builder)

    return wrong_credentials(response_builder)


def do_logout(request, response_builder):
    session_id = request.get_session_id()
    SessionsDAOFactory.get_storage(IN_MEMORY).delete_session(session_id)

    return do_redirect(INDEX_PAGE, response_builder)


def __validate_user(username, password):
    return UsersDAOFactory.get_storage(IN_MEMORY).validate_user(username, password)
