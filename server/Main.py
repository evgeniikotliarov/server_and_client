import server.RequestParser as RequestParser
import server.RequestTransformer as RequestTransformer
from util.constants.const_main import *
from server.Multipart import *

serversocket = socket.socket(socket_family, socket_type)
if reuse_adress: serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((HOST, PORT))
serversocket.listen()

connection, address = serversocket.accept()
raw_request = RequestParser.get_raw_request(connection)

request = RequestTransformer.transform_request(raw_request)
file_to_write = connection.makefile(WRITE_BUFFER, 0)

if is_multipart(request) and methods_allows_action(request):
    multipart_fields = wrap_multipart(request)
    #TODO implement the usage of multipart fields

print(request.headers)
print(request.target)
