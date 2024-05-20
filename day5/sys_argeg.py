import sys

def div(num1 , num2):
    divison = num1/num2
    return divison    
div(4, 10)

def add(a, b):
    result = a+b
    return result
    print("the addition of 2 num is :",result)


num1 = float(sys.argv[1])
operatio = sys.argv[2]
num2 = float( sys.argv[3])

if operatio == "add" :
    output = add(num1,num2)
    print(output)

    # cmnd line to run this code we have to pass num1 and num2 along with cmnd in terminal
    # amnd : python sys_argeg.py 10 add 29
    # here python and filename  value operation value of num2 