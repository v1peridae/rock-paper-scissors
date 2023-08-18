import random

rounds = int(input("How many rounds would you like to play?"))

for x in range (rounds):
    player_move = input("Enter a choice (rock, paper, scissors): ")
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    print(f"\nYou chose {player_move}, computer chose {computer_move}.\n")

    if player_move == computer_move:
        print(f"Both players selected {player_move}. It's a tie!")
        
    elif player_move == "rock":
        if computer_move == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_move == "paper":
        if computer_move == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_move == "scissors":
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    x=x+1
