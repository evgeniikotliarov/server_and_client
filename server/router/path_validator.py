import os.path
from definitions import PUBLIC_FOLDER

def file_exists(file_name):
    if is_allowed_directory(file_name):
        return os.path.exists(file_name) and not os.path.isdir(file_name)
    return False

def is_allowed_directory(file_name):
    requested_path = os.path.abspath(os.path.join(PUBLIC_FOLDER, file_name))
    common_prefix = os.path.commonprefix([requested_path, PUBLIC_FOLDER])
    return common_prefix == PUBLIC_FOLDER

def strip_slash(file_name):
    return file_name.strip('/')

def get_file(file_name):
    if file_exists(os.path.join(PUBLIC_FOLDER, strip_slash(file_name))):
        return os.path.join(PUBLIC_FOLDER, strip_slash(file_name))
    return 'not found' #TODO implement