from storage.users import *

def do_register(request, response_builder):
    print('Requested register')

class Registration():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create(self):
        try:
            return UsersDAO.create_user(self.username, self.password)
        except UserCreationError as err:
            return str(err)
