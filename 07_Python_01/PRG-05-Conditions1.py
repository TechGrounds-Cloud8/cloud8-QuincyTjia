#I declared my input fuction here. 
name_input = input("Please input your name: ")

#I used a condition to check if the input name is correct. 
#When it is my name, it will say hello, welcome. When it is another name, it will say, you are not Quincy.
if name_input == "Quincy":
    print("Hello! Welcome, Quincy!")
else:
    print("Your are", name_input , ", you are not Quincy, get out!")

