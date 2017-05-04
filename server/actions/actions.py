import util.constants.response_codes as codes

from util.path import get_filesystem_path


def do_head(request, response_builder):
    ok_code, ok_message = codes.OK
    connection = request.get_connection()

    response_builder.set_code(ok_code)
    response_builder.set_message(ok_message)
    response_builder.set_connection(connection)
    return response_builder


def do_get(request, response_builder):
    response_builder = do_head(request, response_builder)
    source = get_filesystem_path(request.target)
    response_builder.set_file_and_fileheaders(source)

    return response_builder


def do_options(request, response_builder):
    pass

def do_post(request, response_builder):
    pass

def do_put(request, response_builder):
    pass