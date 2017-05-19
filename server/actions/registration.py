import util.constants.response_codes as codes
from paths import LOGIN_PAGE
from server.form_encodings.decoder import decode_body
from storage.users import UsersDAO
from util.redirect import do_redirect


def do_register(request, response_builder):
    parse_request = decode_body(request)
    name = parse_request["user"]
    password = parse_request["password"]

    UsersDAO.create_user(name, password)

    return do_redirect(LOGIN_PAGE, response_builder)