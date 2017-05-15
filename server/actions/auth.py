from storage.users import UsersDAO
from storage.sessions import SessionsDAO
from server.form_encodings.decoder import decode_body
import util.constants.response_codes as codes
from util.constants.paths import INDEX_PAGE

def do_auth(request, response_builder):
    a_user = decode_body(request.body)
    username = a_user['user']
    password = a_user['password']
    valid_user = __validate_user(username, password)
    if valid_user:
        session_id = SessionsDAO.create_session(username, 12312).encode()
        response_builder.set_cookie(b"session=%s" % session_id)  # TODO COOKIE EXPIRATION

        code, message = codes.SEE_OTHER
        response_builder.set_code(code)
        response_builder.set_message(message)
        response_builder.set_location(INDEX_PAGE)

     #  TODO if not valid redirect
    return response_builder

def __validate_user(username, password):
    try:
        UsersDAO.validate_user(username, password)
        current_user = UsersDAO.get_user(username)
        return True
    except ValueError:
        return False