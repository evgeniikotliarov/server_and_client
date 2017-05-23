import os.path
from util.strings import ensure_string
from paths import PUBLIC_FOLDER, COMPONENTS_FOLDER


def validate_path(requested_path):
    path = get_public_path(requested_path)
    component_path = get_component_path(requested_path)
    if not (file_exists(path) or file_exists(component_path)):
        return False
    if not (is_allowed(path) or is_allowed(component_path)):
        return False
    return True


def file_exists(file_name):
    return os.path.exists(file_name) and not os.path.isdir(file_name)


def is_allowed(file_name):
    requested_path = os.path.abspath(os.path.join(PUBLIC_FOLDER, file_name))
    common_prefix = os.path.commonprefix([requested_path, PUBLIC_FOLDER])
    return common_prefix == PUBLIC_FOLDER


def get_public_path(raw_path):
    return os.path.join(PUBLIC_FOLDER, strip_slashes(raw_path))


def get_component_path(component_raw_path):
    raw_path = next(ensure_string(component_raw_path))
    return os.path.join(COMPONENTS_FOLDER, strip_slashes(raw_path))


def strip_slashes(file_name):
    return file_name.strip('/')