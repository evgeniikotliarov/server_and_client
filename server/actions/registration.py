import util.constants.response_codes as codes
from paths import INDEX_PAGE
from server.form_encodings.decoder import decode_body
from storage.users import UsersDAO


def do_register(request, response_builder):
    parse_request = decode_body(request)
    name = parse_request["user"]
    password = parse_request["password"]

    UsersDAO.create_user(name, password)

    code, message = codes.SEE_OTHER
    response_builder.set_code(code)
    response_builder.set_message(message)
    response_builder.set_location(INDEX_PAGE.encode())

    return response_builder