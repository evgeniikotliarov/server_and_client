import unittest
from server.url_encoder import *

class TestUrlEncoder(unittest.TestCase):

    def test_url_encoder(self):
        user_url = 'name=vasya&password=123456&age=120'
        url_parser = string_parser(user_url)
        result = {'name': 'vasya', 'password': '123456', 'age': '120'}
        self.assertEqual(result, url_parser)

if __name__ == '__main__':
    unittest.main()