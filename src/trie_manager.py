from trie import Trie
import damerau_levenshtein as dl

class TrieManager:
    """Handles the actions between the user and the trie structure."""

    def __init__(self):
        self.trie = Trie()

    def insert_vocabulary(self, files):
        """Inserts a whole vocabulary to the trie structure.

        Args:
            files (list): List of paths to the vocabulary files
        """

        for file in files:
            with open(file, encoding="utf-8") as f:
                content = f.read().splitlines()
                for word in content:
                    self.trie.insert_word(word)

    def insert_word(self, word, file):
        """Inserts a single word to the trie structure and to a file.

        Args:
            word (string): The word to be inserted
            file (string): The name of the file where the word will be added
        """
        with open(file, "a", encoding="utf-8") as f:
            f.write(word + "\n")
        self.trie.insert_word(word)

    def search_word(self, word):
        """Searches the given word from the trie structure.

        Args:
            word (string): The word to be searched

        Returns:
            boolean: If the word was found or not
        """
        return self.trie.search_word(word)

    def get_distances(self, typo, files):
        """Calls the damerau_levenshtein function and gives it the words to compare.

        Args:
            typo (string): The mistyped word from user
            files (list): List of files to get words from

        Returns:
            tuple: The closest word and its distance from typo
        """
        min_distance = 100
        closest = ""
        for file in files:
            with open(file, encoding="utf-8") as f:
                content = f.read().splitlines()
                for word in content:
                    distance = dl.damerau_levenshtein(typo, word)
                    if distance < min_distance:
                        min_distance = distance
                        closest = word
        return (closest, min_distance)
