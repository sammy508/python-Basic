class person:
    def __init__(self, name, age) :

        self.name = name
        self.age = age

p1 = person("sammy", 23)
print(p1.name) 
print(p1.age) 
print("\n") 


class Bikes :
    def __init__(self,brand, model, colour, type,) :
     self.brand = brand
     self.model = model
     self.colour = colour
     self.type = type

    def __str__(self) :
     return  f"{self.brand} {self.colour}"

b1 = Bikes("harley","CVO™ PAN AMERICA®","black","touring") 

print(b1)
print("\n")

# def __str__(self):: This defines the string representation method (__str__). This method is called when str() or print() is used on an instance of the class.
# return f"{self.name}({self.age})": This returns a formatted string showing the name and age of the instance in the format Name(Age).
     


class Me:
   def __init__(self,name,age,gender) :
      self.name = name
      self.age = age
      self.gender = gender

   def myfunction(self)  :
      print("hello i am ",self.name)
m1 = Me("samir",23,"male")      
m1.myfunction()
print("\n")
# 
# here we can set values later also
m1.age= 24
print(m1.age)

# to delete
del(m1.age)
m1.myfunction()

      
          
        