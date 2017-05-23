import unittest
from template_engine.base_view import *

class TestBaseView(unittest.TestCase):
    def test_insert(self):
        test_str = "My test content"
        view = insert_content(test_str)
        self.assertTrue(test_str in view)