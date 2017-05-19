import util.constants.response_codes as codes
from paths import *
from server.form_encodings.decoder import decode_body
from storage.sessions import SessionsDAO
from storage.users import UsersDAO
from util.constants.const_main import SESSION, SESSION_DEFAULT_AGE
from util.redirect import do_redirect


def do_auth(request, response_builder):
    a_user = decode_body(request)
    username = a_user['user']
    password = a_user['password']
    valid_user = __validate_user(username, password)
    if valid_user:
        session_id = SessionsDAO.create_session(username, SESSION_DEFAULT_AGE).encode()
        response_builder.set_cookie(b"%s=%s" % (SESSION, session_id))  # TODO COOKIE EXPIRATION

        return do_redirect(INDEX_PAGE, response_builder)
    else:
        return do_redirect(LOGIN_PAGE, response_builder)

     #  TODO show some error on the page

def __validate_user(username, password):
    try:
        UsersDAO.validate_user(username, password)
        return True
    except ValueError:
        return False