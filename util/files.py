import mimetypes

from .constants.const_main import READ_BUFFER, READ


def retrieve_file(file_path):
    with open(file_path, READ) as source:
        return source.read()


def retrieve_file_buffered(file_path):
    with open(file_path, READ_BUFFER) as source:
        return source.read()


def get_file_type(file_path):
    mime, encoding = mimetypes.guess_type(file_path.decode())
    return mime.encode()
