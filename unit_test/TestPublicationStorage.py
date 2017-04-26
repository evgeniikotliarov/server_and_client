import unittest
import storage.data_storages.memory.PublicationsStorage as publication_storage
from storage.entities.Publication import Publication

class TestPublicationsStorage(unittest.TestCase):

    def test_create_publication(self):
        result = publication_storage.create_publication('Vasya', 'test', 'text')
        self.assertTrue(isinstance(result, Publication))

    def test_get_publication(self):
        pass

    def test_generate_id(self):
        test_unique_number = publication_storage.generate_id()

if __name__ == '__main__':
    unittest.main()