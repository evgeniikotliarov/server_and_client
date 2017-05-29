import unittest
from template.base_view import *

class TestBaseView(unittest.TestCase):
    def test_insert(self):
        test_str = "My test content"
        view = insert_content(test_str)
        self.assertTrue(test_str in view)