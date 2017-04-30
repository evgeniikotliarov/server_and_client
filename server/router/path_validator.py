import os.path
from settings import PUBLIC_FOLDER
from util.constants.const_main import METHODS_ALLOWING_ACTION

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

def method_allows_action(request):
    return request.method in METHODS_ALLOWING_ACTION
