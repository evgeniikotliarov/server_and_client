from storage.users import *
from server.form_encodings.decoder import decode_body
from storage.users import UsersDAO
from util.redirect_generator import redirect_builder
import util.constants.response_codes as codes
from util.constants.paths import INDEX_PAGE

def do_register(request, response_builder):
    parse_request = decode_body(request.body)
    name = parse_request["user"]
    password = parse_request["password"]

    UsersDAO.create_user(name, password)

    created_code, created_message = codes.CREATED
    response_builder.set_code(created_code)
    response_builder.set_message(created_message)

    redirect = redirect_builder(INDEX_PAGE)
    response_builder.set_redirect(redirect)

    return response_builder