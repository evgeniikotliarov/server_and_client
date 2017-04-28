import socket

CRLF = '\r\n'
LF = '\n'

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

POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'
DELETE = 'DELETE'

GET = 'GET'
HEAD = 'HEAD'
OPTIONS = 'OPTIONS'

METHODS_ALLOWING_ACTION = [POST, PUT, PATCH]
