from storage.entities.User import User

users = {}

def create_user(username, password):
    user = User(username, password)
    users[username] = user
    return user

def get_user(username):
    if username in users.keys():
        return users[username]
    return None

def get_all_users():
    return users