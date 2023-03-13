from random import randint


def main():
    computer_result, human_result = 0, 0

    print(f"[-] Computer result: {computer_result}\n[-] Your result: {human_result}")

    while True:
        print("\n[-] Tossing the dice")
        human_result += randint(1, 6)
        computer_result += randint(1, 6)

        print(f"[-] Your result: {human_result}")

        if input("\n[+] Continue? (for exit enter the no) >> ").strip().lower() == "no":
            print(f"\n[-] Computer result: {computer_result}\n[-] Your result: {human_result}")
            print("[-] You win!") if human_result > computer_result else print(
                "[-] Draw") if human_result == computer_result else print("[-] You lose!")
            break


if __name__ == '__main__':
    print("""
[-] DiceGame Game, by Ayzek Neterro @leasanna
[-]
[-] The basic principle of the dice game
[-] is that each player in turn throws
[-] a certain number of dice (from 1 to 6),
[-] after which the result of the roll (the sum of the points dropped)
[-] is used to determine the winner or loser.
[-] An arbitrary number of throws can be made until the end of the game.
""")

    while True:
        main()

        if input("\n[+] Continue? (for exit enter the no) >> ").strip().lower() == "no":
            print("\n[-] Thanks for playing! :)")
            break
