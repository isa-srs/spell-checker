import unittest
from trie import Trie

class TestTrieStructure(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_insert_word(self):
        self.trie.insert_word("aakkonen")

        self.assertEqual(self.trie.search_word("aakkonen"), True)
        self.assertEqual(self.trie.search_word("apina"), False)

    def test_search_word_returns_correct_boolean(self):
        self.assertEqual(self.trie.search_word("tietokone"), False)
        
        self.trie.insert_word("tietokone")

        self.assertEqual(self.trie.search_word("tietokone"), True)