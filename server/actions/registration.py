from paths import LOGIN_PAGE, ERROR_PAGE
from server.form_encodings.decoder import decode_body
from storage.users import UsersMemoryDAO, UserCreationError
from util.redirect import do_redirect


def do_register(request, response_builder):
    parse_request = decode_body(request)
    name = parse_request["user"].decode().strip()
    password = parse_request["password"].decode().strip()
    try:
        UsersMemoryDAO.create_user(name, password)
    except UserCreationError:
        return do_redirect(ERROR_PAGE, response_builder)  # TODO handle it otherwise
    return do_redirect(LOGIN_PAGE, response_builder)


