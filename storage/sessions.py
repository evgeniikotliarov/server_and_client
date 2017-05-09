import settings
from storage.users import UsersDAO
from server.session import *

class Sessions:

    def create_sessions(self, username, age):
        session = Session(username, age)
        return session