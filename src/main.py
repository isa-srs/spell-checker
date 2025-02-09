import damerau_levenshtein as dl

def main():
    """Starts and runs the program.
    """

    while True:
        typo = input("Syötä väärinkirjoitettu sana: ")
        if typo == "":
            break

        correct_spelling = input("Syötä oikeinkirjoitettu sana: ")

        distance = dl.damerau_levenshtein(typo, correct_spelling)

        print(f'Sanojen etäisyys on {distance}.')
        print()

if __name__ == "__main__":
    main()
