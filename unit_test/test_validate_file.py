import os.path
import unittest

from settings import PUBLIC_FOLDER
from server.router.path_validator import *


class TestValidateFile(unittest.TestCase):
    def test_is_directory_allowed(self):
        file = 'styles/style.css'
        result = is_allowed_directory(strip_slash(file))
        self.assertTrue(result)

    def test_directory_is_not_allowed(self):
        file = '../../index.html'
        result = is_allowed_directory(strip_slash(file))
        self.assertFalse(result)

    def test_file_exists(self):
        file = '/index.html'
        result = file_exists(get_public(strip_slash(file)))
        self.assertTrue(result)

    def test_file_not_exists(self):
        file = '/end.html'
        result = file_exists(get_public(strip_slash(file)))
        self.assertFalse(result)

    def test_get_file(self):
        file = '/index.html'
        file_path = get_public(strip_slash(file))
        result = get_file(file)
        self.assertEqual(result, file_path)


def get_public(file_name):
    return os.path.join(PUBLIC_FOLDER, file_name)

def strip_slash(file_name):
    return file_name.strip('/')

if __name__ == '__main__':
    unittest.main()