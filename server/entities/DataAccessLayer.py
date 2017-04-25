class DataAccessLayer:
    def __init__(self, storage):
        self.users = storage.get_users_storage()
        self.publications = storage.get_publications_storage()

    def create_user(self, username, password):
        pass

    def create_publication(self, user_id, title, text):
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
