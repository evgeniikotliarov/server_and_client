import socket

SERVER_NAME = b"Nazvanie servera"

SESSION = b'session'
SESSION_DEFAULT_AGE = 3600 * 24 * 30  # 1 Month in seconds

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
APPEND_BYTE = 'ab'

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

QUERY = "query"
METHOD = "method"
TARGET = "target"
PROTOCOL = "protocol"

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

REGISTER_ACTION_PAGE = b'/register'
AUTH_ACTION_PAGE = b'/auth'
PUBLISH_ACTION_PAGE = b'/publish'
LOGOUT_ACTION_PAGE = b'/logout'
EDIT_POST_ACTION_PAGE = b'/edit'
PUBLICATION_PAGE = b'/publication.html'
PROFILE_PAGE = b'/profile.html'
MAIN_PAGE = b'/index.html'
STATIC = b''
EDIT_POST_PAGE = b'/edit_post.html'
DELETE_POST_ACTION_PAGE = b'/delete_post'


DEFAULT_CACHE_CONTROL = b"max-age=3600000"
HTTP_1_1 = b'HTTP/1.1'

IN_MEMORY = 'store_in_memory'
DATABASE = 'store_in_database'