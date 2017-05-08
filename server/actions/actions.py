import util.constants.response_codes as codes
from util.path import get_filesystem_path
from util.constants.const_main import *

from server.actions.publish import do_publish
from server.actions.registration import do_register
from server.actions.auth import do_auth


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
    response_builder.set_file_and_fileheaders(source)
    return response_builder


def do_options(request, response_builder):
    response_builder = do_head(request, response_builder)
    response_builder.set_allow()
    return response_builder


def do_post(request, response_builder):
    path = request.target
    action = post_actions[path]
    return action(request, response_builder)


def do_put(request, response_builder):
    path = request.target
    action = post_actions[path]
    return action(request, response_builder)


post_actions = {
    REGISTER: do_register,
    AUTH: do_auth,
    PUBLISH: do_publish
}

put_actions = {
    PUBLISH: do_publish
}