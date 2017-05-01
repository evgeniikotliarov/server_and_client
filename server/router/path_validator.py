import os.path
from settings import PUBLIC_FOLDER
from util.constants.const_main import METHODS_ALLOWING_ACTION

def get_file_path(file):
    if file_exists(file) and is_allowed(file):
        return os.path.join(PUBLIC_FOLDER, strip_slash(file))
    return None

def file_exists(file_name):
    return os.path.exists(file_name) and not os.path.isdir(file_name)


def is_allowed(file_name):
    requested_path = os.path.abspath(os.path.join(PUBLIC_FOLDER, file_name))
    common_prefix = os.path.commonprefix([requested_path, PUBLIC_FOLDER])
    return common_prefix == PUBLIC_FOLDER

def tronsform_file_path(path):
    return os.path.join(PUBLIC_FOLDER, strip_slash(path))

def method_allows_action(request):
    return request.method in METHODS_ALLOWING_ACTION

def strip_slash(filename):
    return file_name.strip(b'/')
