from util.constants.const_main import IN_MEMORY, DATABASE
from storage.DAO.publications import Publications
from storage.data_storages.memory import publications_storage


class PublicationsDAOFactory:
    @staticmethod
    def get_storage(storage_type):
        if storage_type == IN_MEMORY:
            return Publications(publications_storage)
        if storage_type == DATABASE:
            return None #TODO to be added