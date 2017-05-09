import os.path
from util.strings import ensure_string
from settings import PUBLIC_FOLDER


def validate_path(requested_path):
    path = get_filesystem_path(requested_path)
    if not file_exists(path) or not is_allowed(path):
        pass # TODO respond with error


def file_exists(file_name):
    return os.path.exists(file_name) and not os.path.isdir(file_name)


def is_allowed(file_name):
    requested_path = os.path.abspath(os.path.join(PUBLIC_FOLDER, file_name))
    common_prefix = os.path.commonprefix([requested_path, PUBLIC_FOLDER])
    return common_prefix == PUBLIC_FOLDER


def get_filesystem_path(raw_path):
    return os.path.join(PUBLIC_FOLDER, strip_slashes(raw_path))


def strip_slashes(file_name):
    return file_name.strip('/')