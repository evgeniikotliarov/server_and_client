import unittest
from server.actions.registration import *


username = 'user'
password = 'password'
class TestRegistration(unittest.TestCase):

    def test_create(self):
        user = Registration(username, password)
        user.create()
        current_user = Users().get_user(username)
        users = Users().get_all_users()
        self.assertTrue(current_user in users.values())
        self.assertTrue(current_user.name, username)
        self.assertTrue(current_user.password, password)

if __name__ == '__main__':
    unittest.main()