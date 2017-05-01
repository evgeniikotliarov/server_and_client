import os
from settings import *
from server.router.path_validator import *

def route(request):
    requested_path = request.path
    file = get_filesystem_path(requested_path)
    if not file_exists(file): return None #TODO implement error codes

def get_filesystem_path(raw_path):
    return os.path.join(PUBLIC_FOLDER, strip_slashes(raw_path))

def strip_slashes(file_name):
    return file_name.strip(b'/')