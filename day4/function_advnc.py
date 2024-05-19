def add(a, b):
    result = a+b
    print("the addition of 2 num is :",result)
add(5, 10)


# here we make a function with parameter which takes a and b 
# as functional parameter and we pass the value to the parameter through add(5, 10)



# We can solve this by using return method this approach also
# which increase modularity of a function   
# return will return the value of a particular function program is executed here print(div(20, 10)  ) and replace the value with given output

def div(num1 , num2):
    divison = num1/num2
    return divison      

  
print(div(20, 10)  )