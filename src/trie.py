class Node:
    def __init__(self):
        self.children = {}
        self.is_terminal = False
    

def insert_word(root, word):
    current = root
    for char in word:
        if char not in current.children:
            new = Node()
            current.children[char] = new

        current = current.children[char]
    current.is_terminal = True

def search_word(root, word):
    current = root
    for char in word:
        if char not in current.children:
            return False
        current = current.children[char]
    return current.is_terminal

# test
root = Node()
with open("src/data/sanasto.txt") as f:
    content = f.read().splitlines()
    for word in content:
        insert_word(root, word)
    

search_words = ["koira", "kala", "aakkonen"]
for word in search_words:
    print(f"Sana: {word}")
    if search_word(root, word):
        print("Löytyy")
    else:
        print("Ei löydy")