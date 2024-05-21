import sys

type = sys.argv[1]

if type == "t2.micro":
 print("it will inject t2.micro on code")
elif type == "t3.medium":
 print("it will inject t3.medium")
else:
 print("please provide a valid instance")
