from storage.users import *

class Registration():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def create(self):
        try:
            return Users().create_user(self.username, self.password)
        except UserCreationError as err:
            return str(err)
