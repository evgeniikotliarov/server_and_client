import uuid
from storage.entities import Publication

class PublicationsStorage:
    def __init__(self, user, publication):
        self.publications = {}

    def create_publication(self, username, title, text, attachment):
        publication = Publication(username, title, text, attachment)
        id = self.generate_id()
        self.publications[id] = publication

    def get_publication(self, id):
        if id in self.publications.keys():
            return self.publications[id]
        return None

    def generate_id(self):
        id = uuid.uuid4()
        return id
        # TODO