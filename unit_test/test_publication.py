import unittest
from storage.publications import *
from storage.entities.publication import Publication

class TestPublication(unittest.TestCase):

    def test_generate_publication(self):
        author = [str(i) for i in range(0, 5)]
        title = [str(i) for i in range(0,10)]
        text = [str(i) for i in range(0,20)]
        for i in range(1,21):
            PublicationsMemoryDAO.create_publication(author, title, text)


    def test_get_n_last_publication(self):
        self.test_generate_publication()
        result = PublicationsMemoryDAO.get_n_last_publications(10)
        self.assertTrue(isinstance(result[0], Publication))

    def test_quantity_publication(self):
        self.test_generate_publication()
        result = len(PublicationsMemoryDAO.get_n_last_publications(9))
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()