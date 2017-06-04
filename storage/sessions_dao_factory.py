from util.constants.const_main import IN_MEMORY, DATABASE
from storage.DAO.sessions import Sessions
from storage.data_storages.memory import sessions_storage


class SessionsDAOFactory:
    @staticmethod
    def get_storage(storage_type):
        if storage_type == IN_MEMORY:
            return Sessions(sessions_storage)
        if storage_type == DATABASE:
            return None  # To be added
