import unittest
from server.request_transformer import *

class TestRequestTransformer(unittest.TestCase):

    def test_proceed_request(self):
        request = "GET /index.html HTTP/1.1"
        result = proceed_request(request)
        self.assertEqual(result.method, "GET")
        self.assertEqual(result.target, "/index.html")
        self.assertEqual(result.protocol, "HTTP/1.1")
        self.assertEqual(result.query, "")
        self.assertEqual(result. headers, "")
        self.assertEqual(result. body, "")

    def test_headers_to_dict(self):
        received = ['Connection: close', 'Allow:blabla']
        expected = {'Connection':'close', 'Allow':'blabla'}
        result = headers_to_dict(received)
        self.assertEqual(result, expected)

    def test_parse_request_line(self):
        request = "GET /index.html HTTP/1.1"
        result = parse_request_line(request)
        self.assertEqual(result['method'], 'GET')
        self.assertEqual(result['target'], '/index.html')
        self.assertEqual(result['query'], '')
        self.assertEqual(result['protocol'], 'HTTP/1.1')

    def test_get_request_regexp(self):
        request = "POST /index.html HTTP/1.1"
        result = Regexes.get_request_regex()
        self.assertRegexpMatches(request, result)

if __name__ == '__main__':
    unittest.main()
