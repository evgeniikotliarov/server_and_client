from util.constants.const_main import IN_MEMORY, DATABASE
from storage.DAO.users import Users
from storage.data_storages.memory import users_storage


class UsersDAOFactory:
    @staticmethod
    def get_storage(storage_type):
        if storage_type == IN_MEMORY:
            return Users(users_storage)
        if storage_type == DATABASE:
            return None  # To be added
