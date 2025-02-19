class Node:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()

            current = current.children[char]
        current.is_terminal = True

    def search_word(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_terminal
