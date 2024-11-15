import os

if(not os.path.exists):
    os.mkdir('codeharry')   # creates folder
    print(os.name)
print(os.getcwd())   # can get the path of current working directoey

os.chdir()   # to change the directory