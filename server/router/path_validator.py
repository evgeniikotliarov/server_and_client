import os.path
from settings import PUBLIC_FOLDER
from util.constants.const_main import METHODS_ALLOWING_ACTION

def file_exists(file_name):
    return os.path.exists(file_name) and not os.path.isdir(file_name)


def is_allowed(file_name):
    requested_path = os.path.abspath(os.path.join(PUBLIC_FOLDER, file_name))
    common_prefix = os.path.commonprefix([requested_path, PUBLIC_FOLDER])
    return common_prefix == PUBLIC_FOLDER

def method_allows_action(request):
    return request.method in METHODS_ALLOWING_ACTION
