import unittest
import storage.data_storages.memory.UsersStorage as user_storage

class TestUsersStorage(unittest.TestCase):

    def test_create_user(self):
        result = user_storage.create_user('Vasya', 'pswd')
        vasya = user_storage.get_user('Vasya')
        self.assertEqual(result, vasya)

    def test_get_user(self):
        vasya = user_storage.get_user('Vasya')
        self.assertTrue(vasya)

    def test_get_all_users(self):
        result = user_storage.create_user('Vasya', 'pswd')
        users = user_storage.get_all_users()
        self.assertEqual(users['Vasya'], result)

if __name__ == '__main__':
    unittest.main()