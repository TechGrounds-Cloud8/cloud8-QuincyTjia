import random

game = True

while game:
    user_move = input("Rock, paper or scissors?: ")
    actions = ["rock", "paper", "scissors"]
    computer_choice = random.choice(actions)

    print("My choice:", user_move, ", The computer chose:", computer_choice)

    if user_move == computer_choice:
        print("It's a tie!")
    elif user_move == "rock":
        if computer_choice == "scissors":
            print("Rock wins of scissors. I win!")
        else:
            print("Paper wins of rock. You lose!")
    elif user_move == "paper":
        if computer_choice == "rock":
            print("Paper wins of rock. I win!")
        else:
            print("Scissors wins of paper. You lose!")
    elif user_move == "scissors":
        if computer_choice == "paper":
            print("Scissors wins of paper.You lose!")
        else:
            print("Rock wins of scissors. I win!")
            
        break


