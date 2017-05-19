import unittest
import uuid

from storage.entities.session import *

session = Session()
session.generate_id()

class TestSession(unittest.TestCase):

    def test_generate_id(self):
        self.assertTrue(type(session._id) is uuid.UUID)
        self.assertTrue(session.age, time.time())

    def test_update_session_age(self):
        session.update_age()
        self.assertTrue(session.age, time.time())

print(time.time())
if __name__ == '__main__':
    unittest.main()