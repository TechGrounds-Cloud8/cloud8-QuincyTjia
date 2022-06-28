#Here I stated that the loop will keep running untill the run is False.
run = True
while run:

    number_input = int(input("Please input a number: "))

    if number_input == 100:
        print(number_input, "is a nice number indeed")
        run = False                                             #Here the loop will stop when the number 100 is guesssed.
    elif number_input < 100:
        print(number_input, "is pretty low, isn't it")
    elif number_input > 100:
        print("Wow, ", number_input, "is a big number!")
        continue                                                #Continue means the loop whill keep running untill a condition is false.

    