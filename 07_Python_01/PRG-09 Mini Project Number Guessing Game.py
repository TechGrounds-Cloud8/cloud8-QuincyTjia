import random

number = random.randint(0, 100)
game = True
guesses = 1

while game:
    number_input = int(input("Please input a number: "))

    if number_input == number:
        print("Thats the right number. You win! Your score is: ", guesses)
        game = False
    elif number_input < number:
        print("Thats the wrong number. You need to go higher.")
        guesses = guesses + 1
    elif number_input > number:
        print("Thats not the right number. You need to go lower.")
        guesses = guesses + 1
        continue


