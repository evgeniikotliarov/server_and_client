from storage.data_storages.memory import session_storage

class Sessions:
    def __init__(self, storage):
        self.storage = storage

    def create_sessions(self, username, age):
        return self.storage.create_session(username, age)

SessionsDAO = Sessions(session_storage)

