# import unittest
#
#
# from server.actions.auth import *
#
# user = UsersMemoryDAO.create_user('vasya', 'pwd')
#
#
# class TestAuthentication(unittest.TestCase):
#
#     def test_generate_session_id(self):
#         auth.generate_session_id()
#         self.assertTrue(auth)
#
#     def test_current_user(self):
#         generate_id(auth)
#         current_user = auth.get_current_user()
#         self.assertEqual(UsersMemoryDAO.get_user('vasya'), current_user)
#
#     def test_user_not_found(self):
#         result = generate_id(auth2)
#         self.assertEqual('user not found', result)
#
#     def test_validate_session_id(self):
#         generate_id(auth)
#         _id = auth.current_user.session
#         self.assertTrue(auth.validate_session_id(_id))
#
#     def test_session_id_is_not_valid(self):
#         generate_id(auth)
#         _id = uuid.uuid4()
#         self.assertFalse(auth.validate_session_id(_id))
#
#
# def generate_id(authorization):
#     return authorization.generate_session_id()
#
# if __name__ == '__main__':
#     unittest.main()