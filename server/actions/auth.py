import util.constants.response_codes as codes
from paths import *
from server.form_encodings.decoder import decode_body
from storage.sessions import SessionsMemoryDAO
from storage.users import UsersMemoryDAO
from util.constants.const_main import SESSION, SESSION_DEFAULT_AGE
from util.redirect import do_redirect, wrong_credentials


def do_auth(request, response_builder):
    a_user = decode_body(request)
    username = a_user['user'].decode().strip()
    password = a_user['password'].decode().strip()
    valid_user = __validate_user(username, password)

    if valid_user:
        session = SessionsMemoryDAO.create_session(username, SESSION_DEFAULT_AGE)
        response_builder.set_cookie(b"%s=%s; max-age=%d" %
                                    (SESSION, session.get_id().encode(), session.max_age, ))
        return do_redirect(INDEX_PAGE, response_builder)
    else:
        return wrong_credentials(response_builder)


def do_logout(request, response_builder):
    session_id = request.get_session_id()
    SessionsMemoryDAO.delete_session(session_id)
    return do_redirect(INDEX_PAGE, response_builder)


def __validate_user(username, password):
    try:
        UsersMemoryDAO.validate_user(username, password)
        return True
    except ValueError:
        return False