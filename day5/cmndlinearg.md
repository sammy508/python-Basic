### command line variable and command line arguments

# Reading and writing variables in python


# Python Command Line Arguments
Python Command Line Arguments provides a convenient way to accept some information at the command line while running the program. We usually pass these values along with the name of the Python script.

To run a Python program, we execute the following command in the command prompt terminal of the operating system. For example, in windows, the following command is entered in Windows command prompt terminal.

If the program needs to accept input from the user, Python's input() function is used. When the program is executed from command line, user input is accepted from the command terminal.
# example
name = input("Enter your name: ")
print ("Hello {}. How are you?".format(name))

# sys in python
    The sys module in Python provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is part of the standard library, so you don't need to install it separately. Here are some common uses and functionalities of the sys module:

    Common Uses and Functionalities:

    1. Command-line Arguments (sys.argv):


    2.Exiting a Program (sys.exit()):
    import sys

    # Exit the program with status code 0
    sys.exit(0)

   3. Platform Information (sys.platform):

    sys.platform provides a string that identifies the platform on which Python is running.

    import sys

    # Print platform
    print("Platform:", sys.platform)


## svg arg[] in python
    sys.argv is a list in Python that contains the command-line arguments passed to a script. The first element, sys.argv[0], is the script name, and the subsequent elements are the additional arguments.

# example

import sys

print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

# Run this script from the command line
python example.py arg1 arg2 arg3

# output will be
Script name: example.py
Arguments: ['arg1', 'arg2', 'arg3']


