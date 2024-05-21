#  Write a  Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))

def find_num(num1, num2):
    result = []
    for number in range (num1, num2+1):
        if number %7 ==0 and number %5 == 0:
            result.append(number)
    return result
number = find_num(num1, num2)

print ("number divisible by 7 and multiple of 5 is : ", number)

# # Here's the output of the given program it only prints number divisible by 7 which is multiple of 5
# enter num1 : 1
# enter num2 : 200
# number divisible by 7 and multiple of 5 is :  [35, 70, 105, 140, 175]