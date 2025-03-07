from trie_manager import TrieManager

vocab = "src/data/sanasto.txt"
user_vocab = "src/data/user_vocabulary.txt"

def actions():
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
    tm.insert_vocabulary(vocab)
    tm.insert_vocabulary(user_vocab)
    print("Sanasto ladattu!")

    while True:
        action = actions()
        
        # tarkista sana
        if action == "1":
            user_word = input("Syötä tarkistettava sana: ")
            if tm.search_word(user_word):
                print("Sana on oikein kirjoitettu.")
            else:
                gd = tm.get_distances(user_word)
                print(f'Tarkoititko sanaa "{gd[0]}"? Sanojen etäisyys on {gd[1]}.')

        # lisää uusi sana
        elif action == "2":
            new_word = input("Syötä uusi lisättävä sana: ")
            if tm.search_word(new_word):
                print(f'Sana "{new_word}" on jo sanastossa.')
            else:
                tm.insert_word(new_word, user_vocab)
                print(f'Sana "{new_word}" lisätty onnistuneesti sanastoon!')

        # poista sana
        elif action == "3" or action == "":
            break
        
        print()

if __name__ == "__main__":
    main()
