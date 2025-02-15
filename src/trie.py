# TODO: refaktoroi

import damerau_levenshtein as dl


class Node:
    def __init__(self):
        self.children = {}
        self.is_terminal = False
    
root = Node()

def insert_word(root, word):
    current = root
    for char in word:
        if char not in current.children:
            new = Node()
            current.children[char] = new

        current = current.children[char]
    current.is_terminal = True

def insert_vocab(file):
    with open(file) as f:
        content = f.read().splitlines()
        for word in content:
            insert_word(root, word)

def search_word(root, word):
    current = root
    for char in word:
        if char not in current.children:
            return False
        current = current.children[char]
    return current.is_terminal

def is_correctly_spelled(word):
    if search_word(root, word):
        return True
    return False

def get_distances(typo):
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

    

if __name__ == "__main__":
    insert_vocab("src/data/sanasto.txt")
    print(is_correctly_spelled("koira"))
    print(get_distances("koimoas"))