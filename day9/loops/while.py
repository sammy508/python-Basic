


# # sasta adder4


# number = int(input("enter number: "))

# sum = 0

# while number != 0:
#     sum = sum+number
#     number = int(input("enter number: "))
# print("the sum is: ", sum)    

# we can also do this as well

def sasta_calculator():
    sum = 0

#The while True loop runs indefinitely until a break condition is met. This loop will keep prompting the user for input.
    while True:
        number = int(input('Enter a number (0 to stop): '))

        if number == 0:
            break  # whie codition is met it breaks the loop
        sum = sum + number
    print("the total sum is:",sum)    
    # Call the function to execute the program
sasta_calculator()    
