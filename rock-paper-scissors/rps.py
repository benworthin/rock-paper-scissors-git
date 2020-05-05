import random

score_one = 0
score_two = 0
game = True
valid_throws = ["rock", "paper", "scissors"]
valid_answers = ["yes", "no"]


def generate_computer_throw():
    random_num = random.randint(1, 3)

    if random_num == 1:
        random_num = "rock"
    elif random_num == 2:
        random_num = "paper"
    elif random_num == 3:
        random_num = "scissors"

    return random_num


def check_if_valid_input(users_input, valid_inputs_array):
    is_valid = False
    for i in valid_inputs_array:
        if users_input == i:
            is_valid = True

    return is_valid


# TODO add support for 2 players
print("Welcome to RPS!")
player_one = input("What is your name? > ")
print(f"{player_one}, you will be playing against the computer.\n")

while game:
    valid_input = False
    while not valid_input:
        player_throw = input("Do you throw Rock, Paper, or Scissors? > ").lower()
        valid_input = check_if_valid_input(player_throw, valid_throws)

        if valid_input:
            print(f"\nYou threw {player_throw}!")
        else:
            print("Invalid throw. Please try again.")

    computer_throw = generate_computer_throw()
    print(f"Computer threw {computer_throw}!")

    if (player_throw == "rock" and computer_throw == "scissors") or (player_throw == "paper" and computer_throw == "rock") or (player_throw == "scissors" and computer_throw == "paper"):
        score_one += 1
        print(player_one + " wins! Computer loses!\n")
    elif (player_throw == "scissors" and computer_throw == "rock") or (player_throw == "rock" and computer_throw == "paper") or (player_throw == "paper" and computer_throw == "scissors"):
        score_two += 1
        print(player_one + " loses! Computer wins!\n")
    elif player_throw == computer_throw:
        print("It's a tie!\n")

    print(f"{player_one}'s score: {score_one}\nComputer's score: {score_two}")

    # Reset variable
    valid_input = False
    while not valid_input:
        play_again = input("Do you want to play again? (Yes/No) > ").lower()
        valid_input = check_if_valid_input(play_again, valid_answers)

        if valid_input:
            if play_again == "yes":
                print("\nLet's start again!")
            else:
                game = False
                print(f"Okay. Good-bye {player_one}!")
        else:
            print("Invalid response. Please try again.")
