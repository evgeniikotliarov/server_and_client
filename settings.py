import os.path
from storage.data_storages.memory import users_storage
from storage.data_storages.memory import publications_storage

ROOT_PATH = os.path.dirname(os.path.abspath(__file__)).encode()
PUBLIC_FOLDER = os.path.join(ROOT_PATH, b'public')

CURRENT_USERS_STORAGE = users_storage
CURRENT_PUBLICATIONS_STORAGE = publications_storage