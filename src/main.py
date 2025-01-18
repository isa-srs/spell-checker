def main():
    while True:
        typo = input("Syötä väärinkirjoitettu sana: ")
        if typo == "":
            break
        print(f'Tarkoititko "{typo}"?')

if __name__ == "__main__":
    main()