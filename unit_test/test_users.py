import unittest
from storage.users import *


def create(user, pwd):
    return UsersDAO.create_user(user, pwd)

username = 'user'
password = 'password'
user = create(username, password)
session_id = '029d0043-6deb-4fa7-af81-4b16f4ac680c'


class TestUsers(unittest.TestCase):

    def test_user_create(self):
        self.assertEqual(user.name, username)
        self.assertEqual(user.password, password)

    def test_get_user(self):
        self.assertEqual(UsersDAO.get_user(username), user)

    def test_user_already_exists(self):
        with self.assertRaises(UserCreationError) as context:
            create(username, password)
        self.assertTrue('User already exist' in str(context.exception))

    def test_get_all_users(self):
        users = UsersDAO.get_all_users()
        self.assertTrue(user in users.values())

    def test_validate_user(self):
        result = UsersDAO.validate_user(username, password)
        self.assertTrue(result)

    def test_user_not_validated(self):
        with self.assertRaises(ValueError) as context:
            UsersDAO.validate_user('user1', 'password1')
        self.assertTrue('Username or password mismatch' in str(context.exception))

    def add_session(self):
        UsersDAO.add_session(user, session_id)
        self.assertEqual(user.session, session_id)

if __name__ == '__main__':
    unittest.main()