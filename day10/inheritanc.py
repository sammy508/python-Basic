# here we use parent class and use super function inside child class 

class person:
    def __init__(self,name,gender,age) :
        self.name = name
        self.age = age
        self.gender = gender

    def printdetail(self) : 
        print(self.name  + self.gender)

class emp(person)  :
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        
x= emp("sammy","male",23)  
x.printdetail()      

