from storage.users import UsersDAO
from server.session import *

from server.form_encodigs.url_encoder import *
import server.response.response_builder as set_cookie


def do_auth(request, response_builder):
    a_user = parse(request.body)
    username = a_user['user']
    password = a_user['password']
    valid_user = _validate_user(username, password)
    if valid_user:
        response_builder.set_cookie("session=%s" % id)


def _validate_user(username, password):
    try:
        UsersDAO.validate_user(username, password)
        current_user = UsersDAO.get_user(username)
        return True
    except ValueError:
        return False


