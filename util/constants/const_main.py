import socket

SERVER_NAME = b"Server server"

CRLF = '\r\n'
LF = '\n'
SPACE = ' '
DOT = b'.'

CRLF_BYTE = CRLF.encode()
LF_BYTE = LF.encode()
SPACE_BYTE = b' '

WRITE_BUFFER = 'wb'
READ_BUFFER = 'rb'
READ = 'r'
READ_PLUS = 'r+'
WRITE = 'w'
WRITE_PLUS = 'w+'
MAKEFILE_BUFFER = 0

EMPTY_STRING = b''
EMPTY_BYTE_STR = b''


BYTE_COLON = b':'

REQUEST_RECV_SIZE = 1024
MAX_CONNECTIONS = 10

HOST = ''
PORT = 3333

reuse_adress = True

socket_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

MULTIPART = b'multipart'

POST = b"POST"
PUT = b"PUT"
PATCH = b"PATCH"
DELETE = b"DELETE"

GET = b"GET"
HEAD = b"HEAD"
OPTIONS = b"OPTIONS"

ACTION_METHODS = [POST, PUT, PATCH]
STATIC_METHODS = [GET, HEAD, OPTIONS]

REGISTER = b'/register'
AUTH = b'/auth'
PUBLISH = b'/publish'

DEFAULT_CACHE_CONTROL = b"max-age=3600000"
HTTP_1_1 = b'HTTP/1.1'

DEFAULT_PATHS = {
    b"/": b"/index.html"
}