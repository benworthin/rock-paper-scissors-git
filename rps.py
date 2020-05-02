import random

game = True
valid_throws = ["Rock", "Paper", "Scissors"]
valid_answers = ["Yes", "No"]


def generate_computer_throw():
    random_num = random.randint(1, 3)

    if random_num == 1:
        random_num = "Rock"
    elif random_num == 2:
        random_num = "Paper"
    elif random_num == 3:
        random_num = "Scissors"

    return random_num


def check_if_valid_throw(users_throw):
    if users_throw == "Rock" or users_throw == "Paper" or users_throw == "Scissors":
        is_valid = True
    else:
        is_valid = False

    return is_valid


print("Welcome to RPS!")
player_one = input("What is your name? > ")
print(player_one + ", you will be playing against the computer.\n")


while game:
    valid_input = False
    while not valid_input:
        player_throw = input("Do you throw Rock, Paper, or Scissors? (type exactly Rock, Paper, or Scissors.) > ")
        valid_input = check_if_valid_throw(player_throw)

        if valid_input:
            print(f"\nYou threw {player_throw}!")
        else:
            print("Invalid throw. Please try again.")

    valid_input = False

    computer_throw = generate_computer_throw()
    print("Computer threw " + computer_throw)

    if (player_throw == "Rock" and computer_throw == "Scissors") or (
            player_throw == "Paper" and computer_throw == "Rock") or (
            player_throw == "Scissors" and computer_throw == "Paper"):
        print(player_one + " wins! Computer loses!\n")
    elif (player_throw == "Scissors" and computer_throw == "Rock") or (
            player_throw == "Rock" and computer_throw == "Paper") or (
            player_throw == "Paper" and computer_throw == "Scissors"):
        print(player_one + " loses! Computer wins!\n")
    elif player_throw == computer_throw:
        print("It's a tie!\n")

    while not valid_input:
        play_again = input("Do you want to play again? (type exactly Yes or No.) > ")
        if play_again == "Yes":
            game = True
            valid_input = True
            print("\nLet's start again!")
        elif play_again == "No":
            game = False
            valid_input = True
            print("Okay. Good-bye!")
        else:
            print("Please enter exactly either Yes or no.")