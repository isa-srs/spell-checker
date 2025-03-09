import unittest
from trie_manager import TrieManager

class TestTrieManager(unittest.TestCase):
    def setUp(self):
        self.tm = TrieManager()
        self.file = "src/data/test_vocabulary.txt"
    
    def test_insert_vocabulary(self):
        self.tm.insert_vocabulary([self.file])
        self.assertEqual(self.tm.search_word("aakkonen"), True)

    def test_insert_word(self):
        self.assertEqual(self.tm.search_word("banaani"), False)
        self.tm.insert_word("banaani", self.file)
        self.assertEqual(self.tm.search_word("banaani"), True)

    def test_get_distances(self):
        dl = self.tm.get_distances("banaan", [self.file])
        self.assertEqual(dl, ("banaani", 1))