import socket

import server.requests.request_parser as request_parser
import server.requests.request_transformer as request_transformer
from server.router import router
from util.constants.const_main import *
from server.response.response_builder import *

socket_server = socket.socket(socket_family, socket_type)
if reuse_adress: socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind((HOST, PORT))
socket_server.listen()

while True:
    connection, address = socket_server.accept()
    raw_request = request_parser.get_raw_request(connection)
    request = request_transformer.transform_request(raw_request) if raw_request else None

    if not request: raise Exception  # TODO proper error response
    request_handler = router.get_request_handler_route(request)
    response_builder = ResponseBuilder()
    response = request_handler(request, response_builder)
    connection.close()