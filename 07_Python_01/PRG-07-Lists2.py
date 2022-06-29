#I create a list of 5 integers here.
numbers = [8, 5, 10, 16, 20]

print("My list: 8, 5, 10, 16, 20")

#I had to use range to give it index numbers and I had to use len to see how many integers there are in the list. 
#The sum is the current value added to the next value from the list. 
#If the last value is reached, the first value from the list will be added.  
for x in range(len(numbers)):

    if x == len(numbers) -1:
        print(numbers[0] + numbers[x])
    
    else:
        sum = (numbers[x] + numbers[x + 1])
        print(sum)
   
