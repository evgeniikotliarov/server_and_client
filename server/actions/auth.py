from storage.users import UsersDAO
from storage.sessions import SessionsDAO
from server.form_encodings._url_encoder import *
import util.constants.response_codes as codes

def do_auth(request, response_builder):
    a_user = parse(request.body)
    username = a_user['user']
    password = a_user['password']
    valid_user = __validate_user(username, password)
    if valid_user:
        print("User valid")
        session_id = SessionsDAO.create_session(username, 12312).encode()
        print(session_id)
        response_builder.set_cookie(b"session=%s" % session_id)  # TODO COOKIE EXPIRATION
        created_code, created_message = codes.CREATED
        response_builder.set_code(created_code)
        response_builder.set_message(created_message)
    #  TODO redirect
     #  TODO if not valid redirect
    return response_builder

def __validate_user(username, password):
    try:
        UsersDAO.validate_user(username, password)
        current_user = UsersDAO.get_user(username)
        return True
    except ValueError:
        return False