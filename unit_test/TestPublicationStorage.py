import unittest
import storage.data_storages.memory.PublicationsStorage as publication_storage
from storage.entities.Publication import Publication

class TestPublicationsStorage(unittest.TestCase):

    def test_create_publication(self):
        result = publication_storage.create_publication('Vasya', 'test', 'text')
        self.assertTrue(isinstance(result, Publication))

    def test_get_publication(self):
        public = publication_storage.create_publication('Document', 'test', 'text')
        all_publications = publication_storage.publications
        doc = all_publications[public.get_id()]
        self.assertEqual(public, doc)

if __name__ == '__main__':
    unittest.main()