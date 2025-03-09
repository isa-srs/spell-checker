class Node:
    """Single node on the trie structure."""

    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    """Trie data structure built of nodes."""

    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        """Inserts a single word to the data structure.

        Args:
            word (string): The word to be inserted
        """

        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]
        current.is_terminal = True

    def search_word(self, word):
        """Searches a word from the data structure.

        Args:
            word (string): The word to be searched.

        Returns:
            boolean: if the word is complete
        """

        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_terminal
