from random import randint


def get_answer(guess: str, random_number: str) -> str:
    if guess == random_number:
        return "Successful"

    for i, element in enumerate(guess):
        if element == random_number[i]:
            return "Fermi"

    return "Pico" if [True for i in guess if i in random_number] else "NumberGuessingGame"


def main() -> None:
    random_number: str = str(randint(100, 999))

    for i in range(10):
        guess: str = input("\n[+] Enter the number >> ")

        if not guess.isdigit() or len(guess) != 3:
            print("[-] The number must be positive three digits!!")
            continue

        answer: str = get_answer(guess, random_number)

        print(f"[-] {answer}.")

        if answer == "Successful":
            break

        print(f"[-] There are {9 - i} attempts left")
    else:
        print("[-] The number of attempts has ended!")


if __name__ == '__main__':
    print("""
[-] NumberGuessingGame, a deductive logic game, by Ayzek Neterro @leasanna
[-] 
[-] I am thinking of a 3-digit number. Try to guess what it is.
[-] Here are some clues:
[-] 
[-] When I say:     That means:
[-]     Pico            One digit is correct but in the wrong position.
[-]     Fermi           One digit is correct and in the right position.
[-]     NumberGuessingGame          No digit is correct.
[-] 
[-] I have thought up a number.
[-] 
[-] The number of attempts is 10.
""")

    while True:
        main()

        if input("\n[+] Continue? (for exit enter the no) >> ").strip().lower() == "no":
            print("\n[-] Thanks for playing! :)")
            break
