# import unittest
# from server.actions.publish import *
#
#
# class TestPublish(unittest.TestCase):
#
#     def test_generate_publish(self):
#         author = [str(i) for i in range(0, 5)]
#         title = [str(i) for i in range(0,10)]
#         text = [str(i) for i in range(0,20)]
#         attachments = None
#         unique_id = None
#         for i in range(1,21):
#             PublicationsDAO.create_publication(author, title, text, attachments, unique_id)
#
#     def test_do_publish(self):
#         publication = self.test_generate_publish()
#         response_builder = do_publish(publication)
#         response = response_builder.get_response()
#         code = response.code
#
#         self.assertEqual(code, 201)
#
#     def test_parse_fields(self):
#         pass
#
# if __name__ == '__main__':
#     unittest.main()