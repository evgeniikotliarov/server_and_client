import unittest

from server.multipart import *
from util.request_samples import *
from server.request_transformer import transform_request

class TestMultipart(unittest.TestCase):
    multi = transform_request(multipart_request)
    simple = transform_request(simple_request)
    with_image = transform_request(multipart_with_image)

    def test_is_multipart(self):
        self.assertTrue(is_multipart(self.multi))
        self.assertFalse(is_multipart(self.simple))

    def test_get_boundary(self):
        self.assertEqual(get_boundary(self.multi), multipart_request_boundary)
        self.assertEqual(get_boundary(self.simple), None)

    def test_get_file_part(self):
        multipart_fields = get_multipart_fields(self.with_image)
        self.assertTrue(type(multipart_fields) == list)
        self.assertTrue(len(multipart_fields) == 3)
        self.assertEqual(multipart_fields[1].field_name, b'tel')
        self.assertTrue(len(multipart_fields[2].body) > 100) #file
