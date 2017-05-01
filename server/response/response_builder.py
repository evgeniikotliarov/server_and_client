from datetime import datetime, tzinfo, timedelta
from server.entities.response import Response
from util.constants.headers import *
from util.constants.const_main import *
from uuid import uuid4

class ResponseBuilder:
    def __init__(self):
        self._response = Response()
        self.set_default_headers()

    def set_default_headers(self):
        self.set_protocol(HTTP_1_1)
        self.set_date(self.get_current_date())
        self.set_server(SERVER)

    def set_code(self, code): self._response.code = code

    def set_message(self, msg): self._response.message = msg

    def set_protocol(self, proto): self._response.protocol = proto

    def set_body(self, body): self._response.body = body

    def set_allow(self):
        allow = b"%s: %s" % (ALLOW, ALLOWED)
        self.add_header(allow)

    def set_cache_control(self, age):
        if age < 0: age = 0
        cache_control = b"%s: max-age=%d" % (CACHE_CONTROL, age)
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

    @staticmethod
    def get_current_date():
        now = datetime.now(GMT1())
        formatted_now = now.strftime("%a, %d %b %Y %H:%M:%S %Z")
        return formatted_now.encode()

    @staticmethod
    def generate_etag():
        return str(uuid4())

class GMT1(tzinfo):
    def utcoffset(self, dt):
        return timedelta(hours=0)

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "GMT"