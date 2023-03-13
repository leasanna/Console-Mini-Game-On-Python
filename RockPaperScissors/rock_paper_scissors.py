from random import choice


def main():
    elements: tuple = ("rock", "paper", "scissors")

    computer_choice = choice(elements)

    while True:
        human_choice: str = input("[+] Your choice >> ").strip().lower()

        if human_choice in elements:
            break

        print("\n[-] Please, enter the correct answers!! (rock, paper or scissors)!!\n")

    print(f"[-] Computer choice >> {computer_choice}")

    match (computer_choice, human_choice):
        case "rock", "paper":
            print("[=] You win!")
        case "rock", "scissors":
            print("[=] You lose!")
        case "paper", "rock":
            print("[=] You lose!")
        case "paper", "scissors":
            print("[=] You win!")
        case "scissors", "paper":
            print("[=] You lose!")
        case "scissors", "rock":
            print("[=] You win!")
        case _:
            print("[=] Draw!")


if __name__ == '__main__':
    print("""
[-]Rock Paper Scissors, by Ayzek Neterro @leasanna
[-]
[-]Rules: 
[-]    Rock defeats scissors, paper wings defeat rock and scissors defeat paper.
[-]    If both sides submit the same option, it is considered a draw.
""")

    while True:
        main()

        if input("\n[+] Continue? (for exit enter the no) >> ").strip().lower() == "no":
            print("\n[-] Thanks for playing! :)")
            break
