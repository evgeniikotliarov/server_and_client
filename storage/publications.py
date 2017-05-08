import settings
from util.strings import bytes_to_strings

class Publications:
    def __init__(self, publication_storage):
        self.storage = publication_storage

    def create_publication(self, author, title, text, attachments=None, unique_id=None):
        self.storage.create_publication(author, title, text, attachments, unique_id=unique_id)

    def delete_publication(self, _id):
        self.storage.delete_publication(_id)

    def replace_publication(self, _id, author, title, text):
        self.delete_publication(_id)
        self.create_publication(author, title, text, unique_id=_id)

    def get_publication(self, _id):
        return self.storage.get_publication(_id)

    def get_all_publication(self):
        return self.storage.get_all_publications

    def get_n_last_punlications(self, number=10):
        publications = []
        all_publications = self.storage.get_all_publications()
        for i, publication in enumerate(all_publications.values()):
            if i > number:
                break
            publications.append(publication)
        return publications

PublicationsDAO = Publications(settings.CURRENT_PUBLICATIONS_STORAGE)