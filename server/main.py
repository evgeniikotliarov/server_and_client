import server.request_parser as request_parser
import server.request_transformer as request_transformer
from server.multipart import *
from server.router.path_validator import *
from server.router.action_router import *
from server.router.static_router import *

serversocket = socket.socket(socket_family, socket_type)
if reuse_adress: serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))
serversocket.listen()

while True:
    connection, address = serversocket.accept()
    raw_request = request_parser.get_raw_request(connection)
    request = request_transformer.transform_request(raw_request)

    connection.close()
