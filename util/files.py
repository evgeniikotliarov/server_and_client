import mimetypes
from paths import PUBLIC_FOLDER
from .constants.const_main import *
from os.path import join


def retrieve_file(file_path):
    with open(file_path, READ) as source:
        return source.read()


def retrieve_file_buffered(file_path):
    with open(file_path, READ_BUFFER) as source:
        return source.read()


def get_file_type(file_path):
    mime, encoding = mimetypes.guess_type(file_path)
    return mime.encode()


def save_image(file, filename, file_path=None):
    if not file_path:
        file_path = join(PUBLIC_FOLDER, 'image')
    with open(join(file_path, filename), WRITE_BUFFER) as destination:
        destination.write(file)