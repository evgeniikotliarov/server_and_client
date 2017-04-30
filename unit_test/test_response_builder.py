import unittest
from server.entities.response import *
from util.regexes import *

response = Response()

class TestResponse(unittest.TestCase):
    def test_set_allow(self):
        allow = b"Allow: GET, POST, PUT, DELETE, OPTIONS"
        response.set_allow()
        result = allow in response.headers
        self.assertTrue(result)

    def test_set_cache_control(self):
        cache_control = b'%s: max-age=3600'%CACHE_CONTROL
        response.set_cache_control(3600)
        result = cache_control in response.headers
        self.assertTrue(result)

    def test_set_connection(self):
        connection = b'%s: close'%CONNECTION
        response.set_connection(b'close')
        result = connection in response.headers
        self.assertTrue(result)

    def test_set_content_encoding(self):
        content_encoding = b'%s: gzip'%CONTENT_ENCODING
        response.set_content_encoding(b'gzip')
        result = content_encoding in response.headers
        self.assertTrue(result)

    def test_set_content_language(self):
        content_language = b'%s: ru, en'%CONTENT_LANGUAGE
        response.set_content_language(b'ru, en')
        result = content_language in response.headers
        self.assertTrue(result)

    def test_set_content_length(self):
        content_length = b'%s: 3495'%CONTENT_LENGTH
        response.set_content_length(3495)
        result = content_length in response.headers
        self.assertTrue(result)

    def test_set_date(self):
        date = datetime.now(GMT1())
        formatted_now = date.strftime("%a, %d %b %Y %H:%M:%S %Z")
        date = b'%s: %s' % (DATE, formatted_now.encode())
        response.set_date()
        result = date in response.headers
        self.assertTrue(result)

    def test_set_e_tag(self):
        etag = b'%s: "s"' %ETAG
        response.set_etag(b's')
        result = etag in response.headers
        self.assertTrue(result)

    def test_set_last_modified(self):
        last_modified = b"%s: date" %LAST_MODIFIED
        response.set_last_modified(b'date')
        result = last_modified in response.headers
        self.assertTrue(result)

    def test_set_expires(self):
        expires = b"%s: date" %EXPIRES
        response.set_expires(b'date')
        result = expires in response.headers
        self.assertTrue(result)

    def test_set_location(self):
        loc = b"%s: location" %LOCATION
        response.set_location(b'location')
        result = loc in response.headers
        self.assertTrue(result)

    def test_set_server(self):
        serv = b"%s: my server" %SERVER
        response.set_server(b'my server')
        result = serv in response.headers
        self.assertTrue(result)

    def test_get_set_cookie(self):
        cook = b"%s: cookie" %COOKIE
        response.set_cookie(b'cookie')
        result = cook in response.headers
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()