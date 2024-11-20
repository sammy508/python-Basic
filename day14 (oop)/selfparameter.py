


# Self parameter is ," when we call a method of  objectas myobject.method(arg1, arg2), this automatically converts
#  by python into Myclass,method(myobj, arg1, arg2)" this ia all about self parameter

class College:

    def __init__(self, name, faculty) :
        self.name = name
        self.faclty = faculty

    def Student(self):
        print(f"Hello I am {self.name}, And i am student of {self.faclty}")   

obj = College("Samir", "CCt")
obj.Student()