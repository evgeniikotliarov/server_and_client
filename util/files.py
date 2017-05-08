import mimetypes

from settings import PUBLIC_FOLDER
from .constants.const_main import *
from os.path import join


def retrieve_file(file_path):
    with open(file_path, READ) as source:
        return source.read()


def retrieve_file_buffered(file_path):
    with open(file_path, READ_BUFFER) as source:
        return source.read()


def get_file_type(file_path):
    mime, encoding = mimetypes.guess_type(file_path.decode())
    return mime.encode()


def save_image(file, file_name, file_path = None):
    if not file_path:
        file_path = join(PUBLIC_FOLDER, b'image').decode()
    with open(join(file_path, file_name), WRITE_BUFFER) as destination:
        destination.write(file)

