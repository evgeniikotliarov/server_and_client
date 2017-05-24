from paths import LOGIN_PAGE, ERROR_PAGE
from server.form_encodings.decoder import decode_body
from storage.users import UsersMemoryDAO, UserCreationError
from util.redirect import do_redirect, user_exists
from util.strings import ensure_string


def do_register(request, response_builder):
    body = decode_body(request)
    name, password = ensure_string(body['user'], body['password'])
    name, password = name.strip(), password.strip()
    try:
        UsersMemoryDAO.create_user(name, password)
    except UserCreationError:
        return user_exists(response_builder)

    return do_redirect(LOGIN_PAGE, response_builder)


