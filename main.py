import server.requests.request_parser as request_parser
import server.requests.request_transformer as request_transformer
import server.response.response_transformer as response_transformer
from server.logger import log_request, log_response
from server.response.response_builder import *
from server.router import router



socket_server = socket.socket(socket_family, socket_type)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_server.bind((HOST, PORT))
socket_server.listen()

while True:
    connection, address = socket_server.accept()
    raw_request = request_parser.get_raw_request(connection)
    request = request_transformer.transform_request(raw_request) if raw_request else None

    if not request: continue
    log_request(request)

    response_builder = ResponseBuilder()
    request_handler = router.get_request_handler_route(request)
    response_obj = request_handler(request, response_builder).get_response()
    response = response_transformer.transform_response(response_obj)

    connection.send(response)
    if response_obj.body:
        connection.send(response_obj.body)
    log_response(response_obj)
    connection.close()