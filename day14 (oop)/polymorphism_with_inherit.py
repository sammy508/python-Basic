

# Polymorphism with Inheritance

class Animal:
    def Speak(self):
        raise NotImplementedError("Subclass must be implemented")
    
class Dog(Animal):

    def Speak(self):
        return "Wooof fkoff"
    
class Cat(Animal):
    def Speak(self):
        return "Meaoww"    
    
animals = [Dog(), Cat()]    

for animal in animals:
  print(animal.Speak())