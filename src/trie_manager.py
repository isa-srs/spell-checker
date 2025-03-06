from trie import Trie
import damerau_levenshtein as dl

class TrieManager:
    def __init__(self):
        self.trie = Trie()

    def insert_vocabulary(self, file):
        with open(file) as file:
            content = file.read().splitlines()
            for word in content:
                self.trie.insert_word(word)

    def search_word(self, word):
        return self.trie.search_word(word)

    def get_distances(self, typo):
        min_distance = 100
        closest = ""
        with open("src/data/sanasto.txt") as f:
            content = f.read().splitlines()
            for word in content:
                distance = dl.damerau_levenshtein(typo, word)
                if distance < min_distance:
                    min_distance = distance
                    closest = word
        return (closest, min_distance)
