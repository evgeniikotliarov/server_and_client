from storage import UsersStorge
from storage.data_storages.memory.data import PublicatuonsStorage


def get_users_storage():
    return UsersStorge()

def get_publicationsStorage():
    return PublicatuonsStorage()
