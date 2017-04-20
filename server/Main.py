import socket

import server.Multipart as multi

import server.RequestParser as RequestParser
import server.RequestTransformer as RequestTransformer
from constants.const_main import *

serversocket = socket.socket(socket_family, socket_type)
if reuse_adress: serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, port))
serversocket.listen()

connection, address = serversocket.accept()
raw_request = RequestParser.get_raw_request(connection).decode()

request = RequestTransformer.transform_request(raw_request)

file_to_write = connection.makefile('wb', 0)