import damerau_levenshtein as dl
import trie

def main():
    """Starts and runs the program.
    """

    print("Ladataan sanastoa...")
    trie.insert_vocab("src/data/sanasto.txt")
    print("Sanasto ladattu!")

    while True:
        given_word = input("Syötä sana: ")
        if given_word == "":
            break
        elif trie.is_correctly_spelled(given_word):
            print("Sana on oikein kirjoitettu.")
        else:
            gd = trie.get_distances(given_word)
            print(f'Tarkoititko {gd[0]}? Sanojen etäisyys on {gd[1]}.')
        print()

if __name__ == "__main__":
    main()
