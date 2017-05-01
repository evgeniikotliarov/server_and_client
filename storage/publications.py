
class Publications:
    def __init__(self, publication_storage):
        self.storage = publication_storage

    def create_publication(self, author, title, text, attachments = None, unique_id = None):
        self.storage.create_publication(author, title, text, attachments = None, unique_id = None)

    def delete_publication(self, id):
        self.storage.delete_publication(id)

    def replace_publication(self, id, author, title, text):
        self.delete_publication(id)
        self.create_publication(author, title, text, unique_id=id)

    def get_publication(self, id):
        return self.storage.get_publication(id)

    def get_all_publication(self):
        pass
