from random import randint


def main():
    random_number = randint(1, 10)
    print("[-] ")

    while True:
        guess_number = int(input("\n[+] Enter the number >> "))

        if random_number == guess_number:
            print("[-] You guessed it right!!")
            break
        elif random_number > guess_number:
            print("[-] Higher.")
        else:
            print("[-] Below.")


if __name__ == '__main__':
    print("""
[-] Simple Number Guessing Game, by Ayzek Neterro @leasanna
[-] 
[-] I'm thinking number from 1 to 10. Try to guess what it is.""")

    while True:
        main()

        if input("\n[+] Continue? (for exit enter the no) >> ").strip().lower() == "no":
            print("\n[-] Thanks for playing! :)")
            break
