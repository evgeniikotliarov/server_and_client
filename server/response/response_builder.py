from server.entities.response import Response
from util.constants.headers import *
from util.constants.const_main import *
from util.id_generator import generate_etag
import util.files as Files
import util.date as Date


class ResponseBuilder:
    def __init__(self, response=None):
        self._response = response if response else Response()
        self.set_default_headers()

    def get_response(self): return self._response

    def set_default_headers(self):
        self.set_protocol(HTTP_1_1)
        self.set_date(Date.get_formatted_date())
        self.set_server(SERVER_NAME)

    def set_code(self, code): self._response.code = code

    def set_message(self, msg): self._response.message = msg

    def set_file_and_fileheaders(self, file_path):
        file = Files.retrieve_file(file_path)
        mime = Files.get_file_type(file_path)

        self.set_content_length(len(file))
        self.set_content_type(mime)
        self.set_etag(generate_etag()) # TODO Etags are generated every time file is requested. Change it to hashing
        self.set_cache_control(DEFAULT_CACHE_CONTROL)  # TODO different cache-controls for different MIMES

        self._response.file = file

    def set_protocol(self, proto): self._response.protocol = proto

    def set_body(self, body): self._response.body = body

    def set_allow(self):
        allow = b"%s: %s" % (ALLOW, ALLOWED)
        self.add_header(allow)

    def set_cache_control(self, control):
        cache_control = b"%s: %s" % (CACHE_CONTROL, control)
        self.add_header(cache_control)

    def set_connection(self, connection):
        conn = b"%s: %s" % (CONNECTION, connection)
        self.add_header(conn)

    def set_content_encoding(self, encoding):
        content_encoding = b"%s: %s" % (CONTENT_ENCODING, encoding)
        self.add_header(content_encoding)

    def set_content_language(self, languages):
        content_language = b"%s: %s" % (CONTENT_LANGUAGE, languages)
        self.add_header(content_language)

    def set_content_length(self, length):
        content_length = b"%s: %d" % (CONTENT_LENGTH, length)
        self.add_header(content_length)

    def set_content_type(self, ctype):
        content_type = b"%s: %s" % (CONTENT_TYPE, ctype)
        self.add_header(content_type)

    def set_date(self, date):
        _date = b'%s: %s' % (DATE, date)
        self.add_header(_date)

    def set_etag(self, etag):
        e = b'%s: "%s"' % (ETAG, etag)
        self.add_header(e)

    def set_last_modified(self, date):
        last_modified = b"%s: %s" % (LAST_MODIFIED, date)
        self.add_header(last_modified)

    def set_expires(self, expires_date):
        expires = b"%s: %s" % (EXPIRES, expires_date)
        self.add_header(expires)

    def set_location(self, location):
        loc = b"%s: %s" % (LOCATION, location)
        self.add_header(loc)

    def set_server(self, server):
        serv = b"%s: %s" % (SERVER, server)
        self.add_header(serv)

    def set_cookie(self, cookie):
        coo = b"%s: %s" % (COOKIE, cookie)
        self.add_header(coo)

    def add_header(self, header):
        self._response.headers.append(header)
