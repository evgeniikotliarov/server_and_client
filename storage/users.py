from storage.data_storages.memory import users_storage

class Users:
    def __init__(self, storage):
        self.users = storage

    def create_user(self, username, password):
        if  not self.__user_exist(username):
            self.users.create_user(username, password)
            return self.get_user(username)
        raise UserCreationError('User already exist')

    def get_user(self, username):
        return self.users.get_user(username)

    def get_all_users(self):
        return self.users.get_all_users()

    def validate_user(self, username, password):
        if self.__user_exists(username) and self.__passwords_match(username, password):
            return True
        raise ValueError('Username or Password mismatch')

    def __user_exists(self, username):
        if username in self.users.get_all_users():
            return True
        return False

    def __passwords_match(self, username, password):
        if self.get_user(username).password == password:
            return True
        return False
    @staticmethod
    def add_session(self, user_obj, session_id):
        user_obj.add_session(session_id)
        return 'Session id was added'

UsersDAO = Users(users_storage)


class UserCreationError(Exception):
    pass

