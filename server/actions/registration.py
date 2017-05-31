from paths import LOGIN_PAGE
from server.form_encodings.decoder import decode_body
from storage.DAO.users import UserCreationError
from storage.users_dao_factory import UsersDAOFactory
from util.redirect import do_redirect, user_exists
from util.strings import ensure_string
from util.constants.const_main import IN_MEMORY


def do_register(request, response_builder):
    body = decode_body(request)
    name, password = ensure_string(body['user'], body['password'])
    name, password = name.strip(), password.strip()

    try:
        UsersDAOFactory.get_storage(IN_MEMORY).create_user(name, password)
    except UserCreationError:
        return user_exists(response_builder)

    return do_redirect(LOGIN_PAGE, response_builder)





