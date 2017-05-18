import util.constants.response_codes as codes
from util.path import get_filesystem_path
from util.constants.const_main import *


def do_head(request, response_builder):
    ok_code, ok_message = codes.OK
    connection = request.get_connection()

    response_builder.set_code(ok_code)
    response_builder.set_message(ok_message)
    if connection:
        response_builder.set_connection(connection)
    return response_builder


def do_get(request, response_builder):
    response_builder = do_head(request, response_builder)
    source = get_filesystem_path(request.target)
    response_builder.set_file_and_fileheaders(source, request.get_session())
    return response_builder


def do_options(request, response_builder):
    response_builder = do_head(request, response_builder)
    response_builder.set_allow()
    return response_builder

