from storage.users import UsersDAO
from server.session import *
class Auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session = Session
        self.current_user = None

    def generate_session_id(self):
        if self.__validate_user():
            session_id = self.session.generate_id()
            self.current_user = UsersDAO.get_user(self.username)
            UsersDAO.add_session(self.current_user, session_id)
        return 'User not found'

    def get_current_user(self):
        return self.current_user

    def validate_session_id(self, id):
        valid_id = self.current_user.session
        if id == valid_id:
            self.__update_session_id_age()
            return True
        return False

    def __update_session_id_age(self):
        self.session.update_age()

    def __validate_user(self):
        try:
            UsersDAO.validate_user(self.username, self.password)
            self.current_user = UsersDAO.get_user(self.username)
            return True
        except ValueError:
            return False
