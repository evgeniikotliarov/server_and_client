import os.path
from Definitions import PUBLIC_FOLDER

def file_exists(file_name):
    if is_allowed_directory(file_name):
        return os.path.exists(file_name) and not os.path.isdir(file_name)
    return False

def is_allowed_direct(file_name):
    requested_path = os.path.join(PUBLIC_FOLDER, file_name)
    common_prefix = os.path.commonprefix([requested_path, PUBLIC_FOLDER])
    return common_prefix == PUBLIC_FOLDER

def get_file(file_name):
    if file_exists(os.path.join(PUBLIC_FOLDER, file_name)):
        return os.path.join(PUBLIC_FOLDER, file_name)
    return 'Not found' #TODO implement
