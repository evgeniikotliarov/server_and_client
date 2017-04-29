import unittest
from server.FileRouter import *
from Definitions import *
import os.path

class TestFileRouter(unittest.TestCase):

    def test_is_directory_allowed(self):
        file = '/etc/pwd'
        result = is_allowed_directory(file)
        self.assertEqual(result, False)

    def test_directory_is_not_allowed(self):
        file = 'styles/index.html'
        result = is_allowed_directory(file)
        self.assertEqual(result, True)

    def test_file_exists(self):
        file = 'styles/index.html'
        result = file_exists(get_public(file))
        self.assertTrue(result)

    def test_file_not_exists(self):
        file = 'styles/end.html'
        result = file_exists(get_public(file))
        self.assertEqual(result, False)

    def test_file_absolute_path(self):
        file = 'styles/index.html'
        result = get_file(file)
        self.assertEqual(result, os.path.join(PUBLIC_FOLDER, 'styles/index.html'))

    def test_file_has_wrong_path_and_is_not_traversal(self):
        file = '/styles/index.html'
        result = get_file(file)
        self.assertEqual(result, 'Not found')

def get_public(file_name):
    return os.path.join(PUBLIC_FOLDER, file_name)

if __name__ == '__main__':
    unittest.main()