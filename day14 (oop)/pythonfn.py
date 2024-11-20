
# Python function Arguments

def evenodd(num):
    if(num%2==0):
        print("Even")

    else:
        print("odd")    
evenodd(5)
evenodd(6)        

#  DEfault arguments

def DefaultArg(x, y=50):
    print("x : ", x)
    print("y : ", y)

    # It automtically assign the value to the x
DefaultArg(20)       

# Output
# x :  20
# y :  50



# Arbitary Keyword Arguments

def myfn(*argv):
    for arg in argv:
        print(arg)

myfn('Hello','I am', 'Sammy')

# Output
# Hello
# I am
# Sammy

#  Variabe leth keywords arguments
 # we called it ** kwargs arguments also

def myfn(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s"%(key, value))

myfn(first ='Hello',mid ='I am', last ='Sammy')

# Here it assign the value in %s by position of the arguments

# Output
# first == Hello
# mid == I am
# last == Sammy


# Python Function within Function
# Nested Function

def f1():
    s = "Python for automation"

    def f2():
        print(s)
    f2()
f1()        

# Anonymous Function in Python
# In Python, an anonymous function means that a function is without a name.

def cube(x):return x*x*x
print(cube(5))

# lambda Function
cube_v1 = lambda x:x*x
print(cube_v1(4))


def Swap(x, y):
    return y,x
x,y =  Swap(10,20)
print("a =", x)  # Output: a = 10
print("b =", y)
   