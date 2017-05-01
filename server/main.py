import server.requests.request_parser as request_parser

import server.requests.request_transformer as request_transformer
from server.router import router
from server.router.action_router import *

serversocket = socket.socket(socket_family, socket_type)
if reuse_adress: serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))
serversocket.listen()

while True:
    connection, address = serversocket.accept()
    raw_request = request_parser.get_raw_request(connection)

    request = request_transformer.transform_request(raw_request) if raw_request else None
    if request:
        request.makefile = connection.makefile
        router.route(request)
    connection.close()