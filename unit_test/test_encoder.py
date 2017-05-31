import unittest

from server.form_encodings.url_encoded import *


class TestUrlEncoder(unittest.TestCase):

    def test_url_encoder(self):
        user_url = 'name=vasya&password=123456&age=120'
        url_parser = parse_url_encoded(user_url)
        result = {'name': 'vasya', 'password': '123456', 'age': '120'}
        self.assertEqual(result, url_parser)

if __name__ == '__main__':
    unittest.main()