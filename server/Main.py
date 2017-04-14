import socket
import server.RequestTransformer as RequestTransformer
from constants.misc import *

serversocket = socket.socket(socket_family, socket_type)
if reuse_adress: serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))
serversocket.listen()

connection, address = serversocket.accept()
request_data = connection.recv(REQUEST_RECV_SIZE).decode()

request = RequestTransformer.proceed_request(request_data)
print(request.headers)
file_to_write = connection.makefile('wb', 0)