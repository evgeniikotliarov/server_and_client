from storage.users import UsersDAO
from server.session import *


def do_auth(request, response_builder):
    print("Requested auth")

def _validate_user(self):
    try:
        UsersDAO.validate_user(self.username, self.password)
        self.current_user = UsersDAO.get_user(self.username)
        return True
    except ValueError:
        return False

def set_cookie(response_builder):
    pass

