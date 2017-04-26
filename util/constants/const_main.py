import socket

CRLF = '\r\n'
LF = '\n'

CRLF_BYTE = CRLF.encode()
LF_BYTE = LF.encode()

EMPTY_STRING = ''
EMPTY_BYTE_STR = b''

BYTE_COLON = b':'

REQUEST_RECV_SIZE = 1024
MAX_CONNECTIONS = 10

host = ''
port = 3333

reuse_adress = True

socket_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

MULTIPART = b'multipart'