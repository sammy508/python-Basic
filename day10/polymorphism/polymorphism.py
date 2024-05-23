

# # polymorphism

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():

class car:
    def __init__(self, brand, model, color) :
        self.brand = brand
        self.model = model
        self.color = color
    def move(self):
        print("it runs smoothly")    
class bikes:
    def __init__(self, brand, model, color) :
        self.brand = brand
        self.model = model
        self.color = color
    def move(self):
        print("it runs furiously")    
class bus:
    def __init__(self, brand, model, color) :
        self.brand = brand
        self.model = model
        self.color = color
    def move(self):
        print("it runs fearfully")    

car1 = car("lambo","supra","black")       
bike = bikes("harley","davidputra","black")       
bus1 = bus("tata","night","black")   


for y in (car1,bike, bus1):
    y.move()