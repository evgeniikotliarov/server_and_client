import unittest

from util.path import *

class TestValidateFile(unittest.TestCase):
    def test_is_directory_allowed(self):
        file = b'styles/style.css'
        result = is_allowed(strip_slashes(file))
        self.assertTrue(result)

    def test_directory_is_not_allowed(self):
        file = b'../../index.html'
        result = is_allowed(strip_slashes(file))
        self.assertFalse(result)

    def test_get_filesystem_path(self):
        file = b'/index.html'
        result = get_public_path(file)
        expected = b'/home/evgenii/projects/server_and_client/public/index.html'
        self.assertEqual(result, expected)


    # def test_file_exists(self):
    #     file = b'/index.html'
    #     result = file_exists(transform_file_path(strip_slash(file)))
    #     self.assertTrue(result) # TODO Redo, does two things
    #
    # def test_file_not_exists(self):
    #     file = b'/end.html'
    #     result = file_exists(transform_file_path(strip_slash(file)))
    #     self.assertFalse(result) # TODO does two things, redo

    # def test_get_file(self):
    #     file = b'/index.html'
    #     file_path = transform_file_path(strip_slash(file))
    #     result = get_file_path(file)
    #     self.assertEqual(result, file_path) TODO Write proper test - this one does two things

if __name__ == '__main__':
    unittest.main()