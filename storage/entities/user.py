class User:
    def __init__(self, name, password, session, publication):
        self.name = name
        self.password = password
        self.publication = []
        self.session = None

    def add_session(self, session_id):
        self.sesion = session_id

    def add_publication(self):
        pass
