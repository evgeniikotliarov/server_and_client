import socket

NEWLINE = '\r\n'
EMPTY_STRING = ''

REQUEST_RECV_SIZE = 1024
MAX_CONNECTIONS = 10

host = ''
port = 3333

reuse_adress = True


socket_family = socket.AF_INET
socket_type = socket.SOCK_STREAM