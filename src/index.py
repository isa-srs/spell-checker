from trie_manager import TrieManager

def main():
    """Starts and runs the program.
    """

    tm = TrieManager()

    print("Ladataan sanastoa...")
    tm.insert_vocabulary("src/data/sanasto.txt")
    print("Sanasto ladattu!")

    while True:
        user_word = input("Syötä sana: ")
        if user_word == "":
            break
        elif tm.search_word(user_word):
            print("Sana on oikein kirjoitettu.")
        else:
            gd = tm.get_distances(user_word)
            print(f'Tarkoititko {gd[0]}? Sanojen etäisyys on {gd[1]}.')
        print()

if __name__ == "__main__":
    main()
