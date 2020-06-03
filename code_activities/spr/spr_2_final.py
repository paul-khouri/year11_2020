import random

optionList = ["r", "s", "p"]


def start_text():
    print("-----------------------------------------------")
    print("Play rock , scissors, paper \n"
          "enter your choice and play for best of three")
    print("-----------------------------------------------")


def get_player_input():
    player_choice = input("Rock(r), Scissors(s), Paper(p)   ")
    return player_choice


def get_single_input(t):
    txt = input(t)
    my_text = txt.replace(" ", "")
    my_text = my_text.lower()
    return my_text[0]


def run_game(player_choice):
    computer_choice = random.choice(optionList)
    print("| player: \t{}\n| computer: \t{}".format(player_choice, computer_choice).expandtabs(8))
    if player_choice == computer_choice:
        result = "draw"
    elif computer_choice == "r" and player_choice == "s":
        result = "c_wins"
    elif computer_choice == "r" and player_choice == "p":
        result = "p_wins"
    elif computer_choice == "p" and player_choice == "s":
        result = "p_wins"
    elif computer_choice == "p" and player_choice == "r":
        result = "c_wins"
    elif computer_choice == "s" and player_choice == "p":
        result = "c_wins"
    elif computer_choice == "s" and player_choice == "r":
        result = "p_wins"
    else:
        print("program error working out result")
        return "No game"
    return result


def main():
    p_count = 0
    c_count = 0
    start_text()
    while p_count < 2 and c_count < 2:
        player_choice = get_single_input("Enter Rock(r), Scissors(s), Paper(p):   ")
        result = run_game(player_choice)
        if result == "p_wins":
            p_count += 1
            print("You win")
        elif result == "c_wins":
            print("Computer wins")
            c_count += 1
        else:
            print(result)
    if p_count == 2:
        print("You have won best of three")
    else:
        print("The computer has won best of three")
    print("---------------------------------------")
    cont = get_single_input("Would you like to play again y/n:  ")
    if cont == "y":
        main()


if __name__ == '__main__':
    main()

print("Program has ended")
