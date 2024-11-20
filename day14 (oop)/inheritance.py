class Human(object):

    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


    def isEmployee(self):
        return False

class Employee(Human):
    def isEMployee(self):
        return True

emp = Human("SAmmy")
print(emp.getname(), emp.isEmployee())

emp = Employee("SAmmy")
print(emp.getname(), emp.isEMployee())


        