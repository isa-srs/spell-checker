from trie_manager import TrieManager

FILES = ["src/data/sanasto.txt", "src/data/user_vocabulary.txt"]

def actions():
    """Prints out the instructions / actions that the user can do."""

    print()
    print("TOIMINNOT:")
    print("1: tarkista sanan oikeinkirjoitus")
    print("2: lisää uusi sana")
    print("3 (tai tyhjä syöte): lopeta ohjelma")
    print()

    action = input("Syötä haluamasi toiminnon vastaava numero (1, 2, 3): ")
    print()

    return action


def main():
    """Starts and runs the program."""

    tm = TrieManager()

    print("Ladataan sanastoa...")
    tm.insert_vocabulary(FILES)
    print("Sanasto ladattu!")

    while True:
        action = actions()

        # tarkista sana
        if action == "1":
            user_word = input("Syötä tarkistettava sana: ")
            if tm.search_word(user_word):
                print("Sana on oikein kirjoitettu.")
            else:
                gd = tm.get_distances(user_word, FILES)
                print(f'Tarkoititko sanaa "{gd[0]}"? Sanojen etäisyys on {gd[1]}.')

        # lisää uusi sana
        elif action == "2":
            new_word = input("Syötä uusi lisättävä sana: ")
            if tm.search_word(new_word):
                print(f'Sana "{new_word}" on jo sanastossa.')
            else:
                tm.insert_word(new_word, FILES[1])
                print(f'Sana "{new_word}" lisätty onnistuneesti sanastoon!')

        # poista sana
        elif action in ("3", ""):
            break

        print()

if __name__ == "__main__":
    main()
