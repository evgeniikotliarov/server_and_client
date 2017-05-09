from storage.entities.session import *

class Sessions:

    def create_sessions(self, username, age):
        session = Session(username, age)
        return session