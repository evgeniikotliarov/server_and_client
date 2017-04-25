from server.User import *
from server.Publication import *

class Storage:
    def __init__(self, user, publication):
        self.user = user
        self.publication = publication

    def create_user(self, username, password):
        self.user = User(username, password)
        pass

    def create_publication(self, user_id, title, text):
        self.post = Publication(user_id, title, text)
        pass

    def delete_publication(id):
        pass

    def replace_publication(id):
        pass

    def get_user(username):
        pass

    def get_publication(id):
        pass

    def get_last_publication(num):
        pass

    def get_all_publication(self):
        pass

    def get_all_users(self):
        pass