from storage.data_storages.memory import sessions_storage


class Sessions:

    def __init__(self, storage):
        self.storage = storage

    def create_session(self, username, age):
        return self.storage.create_session(username, age)

    def get_session(self, session_id):
        return self.storage.get_session(session_id)

    def delete_session(self, session_id):
        self.storage.delete_session(session_id)


SessionsMemoryDAO = Sessions(sessions_storage)