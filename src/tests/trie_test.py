import unittest
from trie import Trie

FILE = "src/data/test_vocabulary.txt"

class TestTrieStructure(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_word(self):
        self.trie.insert_word("aakkonen")

        self.assertEqual(self.trie.search_word("aakkonen"), True)
        self.assertEqual(self.trie.search_word("apina"), False)
