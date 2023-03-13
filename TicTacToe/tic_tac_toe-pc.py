from random import choice, randint


def draw_field(field: list) -> None:
    print()

    for i, elm in enumerate(field):
        if not i:
            res = " | ".join(elm).replace("|", " ")
        else:
            res = " | ".join(elm).replace("|", "", 1)

        print(f"[-]\t\t{res}")

    print()


def check_field(field: list) -> tuple:
    for i in range(1, 6, 2):
        elm = [field[i][1], field[i][2], field[i][3]]

        if len(set(elm)) == 1 and elm[0] != "#":
            return True, elm[0]

    for i in range(1, 4):
        elm = [field[1][i], field[3][i], field[5][i]]

        if len(set(elm)) == 1 and elm[0] != "#":
            return True, elm[0]

    diagonals = [[field[1][1], field[3][2], field[5][3]], [field[1][3], field[3][2], field[5][1]]]

    for _, elm in enumerate(diagonals):
        if len(set(elm)) == 1 and elm[0] != "#":
            return True, elm[0]

    return False, None


def check_input_data(data: list):
    if len(data) != 2:
        return

    if not (data[1].isdigit() and 1 <= int(data[1]) <= 3):
        return

    data[1] = 2 * int(data[1]) - 1

    match data[0]:
        case "A":
            return data[1], 1
        case "B":
            return data[1], 2
        case "C":
            return data[1], 3
        case _:
            return


def main() -> bool:
    field = [
        ["", "A", "B", "C"],
        ["1", "#", "#", "#"],
        [" ", "—", "—", "—"],
        ["2", "#", "#", "#"],
        [" ", "—", "—", "—"],
        ["3", "#", "#", "#"],
    ]

    used_slots = list()

    while True:
        draw_field(field)

        while True:
            player1 = check_input_data(list(map(str, input(f"\n[+] {player1_name}'s move >> ").upper().split(" "))))

            if player1 and (player1[0], player1[1]) not in used_slots:
                break

            print("[-] The coordinates are entered incorrectly!")

        field[player1[0]][player1[1]] = "x"

        used_slots.append((player1[0], player1[1]))

        filed_result = check_field(field)

        if filed_result[0]:
            print(f"[+] Win {player1_name}!")
            return True

        while True:
            # player2 = check_input_data(list(map(str, input(f"[+] {player2_name}'s move >> ").upper().split(" "))))
            player2 = check_input_data([choice(("A", "B", "C")), str(randint(1, 3))])

            if player2 and (player2[0], player2[1]) not in used_slots:
                break

            print("[-] The coordinates are entered incorrectly!")

        field[player2[0]][player2[1]] = "O"

        used_slots.append((player2[0], player2[1]))

        filed_result = check_field(field)

        if filed_result[0]:
            print(f"\n[+] Win {player2_name}!")
            return False


if __name__ == '__main__':
    print("""
[-] Tic Tac Toe Game, by Ayzek Neterro @leasanna
[-]
[-] Games for two players.
[-] Enter coordinates in this way: A 1
                                """)
    player1_name = input("[+] Enter the name of the first player >> ")
    player2_name = input("[+] Enter the name of the second player >> ")

    player1_score, player2_score = 0, 0

    while True:
        result = main()

        if result:
            player1_score += 1
        else:
            player2_score += 1

        print(f"\n[-] {player1_name}: {player1_score}\n[-] {player2_name}: {player2_score}")

        if input("\n[+] Continue? (for exit enter the no) >> ").strip().lower() == "no":
            print("\n[-] Thanks for playing! :)")
            break
