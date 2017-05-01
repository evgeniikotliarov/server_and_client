import unittest
import storage.data_storages.memory.publications_storage as publication_storage
from storage.entities.publication import Publication

class TestPublicationsStorage(unittest.TestCase):

    def test_create_publication(self):
        result = publication_storage.create_publication('Vasya', 'test', 'text')
        self.assertTrue(isinstance(result, Publication))

    def test_get_publication(self):
        public = publication_storage.create_publication('Document', 'test', 'text')
        all_publications = publication_storage._publications
        doc = all_publications[public.get_id()]
        self.assertEqual(public, doc)

if __name__ == '__main__':
    unittest.main()