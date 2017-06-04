class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.publications = []
        self.session = None

    def add_session(self, session_id):
        self.session = session_id

    def add_publication(self, publication):
        self.publications.append(publication)

    def get_publications(self):
        return self.publications
