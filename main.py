import random

rounds = int(input("How many rounds would you like to play?"))
player_score = 0
computer_score = 0

for x in range (rounds):
    player_move = input("Your move (rock, paper, scissors): ")
    moves = ["rock", "paper", "scissors"]
    computer_move = random.choice(moves)
    print(f"\nYou chose {player_move}, computer chose {computer_move}.\n")

    if player_move == computer_move:
        print(f"Both players selected {player_move}. It's a tie!")
    elif player_move == "rock":
        if computer_move == "scissors":
            print("Rock smashes scissors! You win!")
            player_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score +=1
    elif player_move == "paper":
        if computer_move == "rock":
            print("Paper covers rock! You win!")
            player_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score +=1
    elif player_move == "scissors":
        if computer_move == "paper":
            print("Scissors cuts paper! You win!")
            player_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score +=1
    x=x+1

print("\nYour score is ",player_score)
print("The computer's score is ", computer_score)
