import util.constants.response_codes as codes
from paths import INDEX_PAGE
from server.form_encodings.decoder import decode_body
from storage.sessions import SessionsDAO
from storage.users import UsersDAO
from util.constants.const_main import SESSION


def do_auth(request, response_builder):
    a_user = decode_body(request)
    username = a_user['user']
    password = a_user['password']
    valid_user = __validate_user(username, password)
    if valid_user:
        session_id = SessionsDAO.create_session(username, 12312).encode()
        response_builder.set_cookie(b"%s=%s" % (SESSION, session_id))  # TODO COOKIE EXPIRATION

        code, message = codes.SEE_OTHER
        response_builder.set_code(code)
        response_builder.set_message(message)
        response_builder.set_location(INDEX_PAGE.encode())

     #  TODO if not valid redirect
    return response_builder

def __validate_user(username, password):
    try:
        UsersDAO.validate_user(username, password)
        return True
    except ValueError:
        return False