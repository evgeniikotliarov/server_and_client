import socket

SERVER = 'Some crappy server'
CRLF = '\r\n'
LF = '\n'

DOT = b'.'

CRLF_BYTE = CRLF.encode()
LF_BYTE = LF.encode()

WRITE_BUFFER = 'wb'
READ_BUFFER = 'rb'
READ = 'r'
READ_PLUS = 'r+'
WRITE = 'w'
WRITE_PLUS = 'w+'

EMPTY_STRING = ''
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

POST = b'POST'
PUT = b'PUT'
PATCH = b'PATCH'
DELETE = b'DELETE'

GET = b'GET'
HEAD = b'HEAD'
OPTIONS = b'OPTIONS'

ACTION_METHODS = [POST, PUT, PATCH]
STATIC_METHODS = [GET, HEAD, OPTIONS]

REGISTER = b'register'
AUTH = b'auth'

DEFAULT_MAX_AGE = 3600000
HTTP_1_1 = 'HTTP/1.1'