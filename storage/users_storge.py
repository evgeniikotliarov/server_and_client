from storage.entities import user

class UsersStorage:
    def __init__(self, user, publication):
        self.users = {}

    def create_user(self, username, password):
        user = user(username, password)
        self.users[username] = user

    def get_user(self, username):
        if username in self.users.keys():
            return self.users[username]
        return None

    def get_all_users(self):
        return self.users