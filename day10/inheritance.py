# class person:
#     def __init__(self, name, gender, age) :
#         self.name = name
#         self.gender = gender
#         self.age = age
#     def printname(self):
#         print(self.name)  
# class emp:
#     def __init__(self) :
#        def __init__(self, name) :
#            person.__init_(self, name) 
# x =   emp("sammy") 
# x.printname()        

class person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def printname(self):
        print(self.name)

class emp(person):  # emp class inherits from person
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)  # Initialize the parent class

# Create an instance of the emp class
x = emp("Sammy", "Male", 30)
x.printname()  # This will print the name "Sammy"
