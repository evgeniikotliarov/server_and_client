import server.request_parser as RequestParser
import server.request_transformer as RequestTransformer
from util.constants.const_main import *
from server.multipart import *
from server.router.path_validator import *
from server.router.action_router import *
from server.router.static_router import *

serversocket = socket.socket(socket_family, socket_type)
if reuse_adress: serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))
serversocket.listen()

connection, address = serversocket.accept()
raw_request = RequestParser.get_raw_request(connection)

request = RequestTransformer.transform_request(raw_request)
file_to_write = connection.makefile(WRITE_BUFFER, 0)

if not file_exists(request, target):
    pass #TODO Error code throwing

if is_multipart(request) and method_allows_action(request):
    multipart_fields = wrap_multipart(request)
    #TODO implement the usage of multipart fields
