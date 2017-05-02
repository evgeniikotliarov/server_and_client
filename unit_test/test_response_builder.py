import unittest
from util.constants.headers import *
from util.date import get_formatted_date
from server.response.response_builder import ResponseBuilder

response_builder = ResponseBuilder()

class TestResponse(unittest.TestCase):
    def test_set_allow(self):
        allow = b"Allow: GET, POST, PUT, DELETE, OPTIONS"
        response_builder.set_allow()
        result = allow in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_cache_control(self):
        expected = b'%s: max-age=3600' % CACHE_CONTROL
        response_builder.set_cache_control(b'max-age=3600')
        result = expected in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_connection(self):
        connection = b'%s: close' % CONNECTION
        response_builder.set_connection(b'close')
        result = connection in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_content_encoding(self):
        content_encoding = b'%s: gzip' % CONTENT_ENCODING
        response_builder.set_content_encoding(b'gzip')
        result = content_encoding in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_content_language(self):
        content_language = b'%s: ru, en' % CONTENT_LANGUAGE
        response_builder.set_content_language(b'ru, en')
        result = content_language in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_content_length(self):
        content_length = b'%s: 3495' % CONTENT_LENGTH
        response_builder.set_content_length(3495)
        result = content_length in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_date(self):
        formatted_date = get_formatted_date()
        date = b'%s: %s' % (DATE, formatted_date)
        response_builder.set_date(date)
        result = date in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_e_tag(self):
        etag = b'%s: "s"' % ETAG
        response_builder.set_etag(b's')
        result = etag in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_last_modified(self):
        last_modified = b"%s: date" % LAST_MODIFIED
        response_builder.set_last_modified(b'date')
        result = last_modified in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_expires(self):
        expires = b"%s: date" % EXPIRES
        response_builder.set_expires(b'date')
        result = expires in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_location(self):
        loc = b"%s: location" % LOCATION
        response_builder.set_location(b'location')
        result = loc in response_builder.get_response().headers
        self.assertTrue(result)

    def test_set_server(self):
        serv = b"%s: my server" % SERVER
        response_builder.set_server(b'my server')
        result = serv in response_builder.get_response().headers
        self.assertTrue(result)

    def test_get_set_cookie(self):
        cook = b"%s: cookie" % COOKIE
        response_builder.set_cookie(b'cookie')
        result = cook in response_builder.get_response().headers
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()