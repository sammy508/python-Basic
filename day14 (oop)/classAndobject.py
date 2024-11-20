

#  Class and pobject

class Animal:

    animal1 = "Dog"
    animal2 = "Cat"

    # sample method
    def Dog(self):
        print(f"{self.animal1} is a pet.")
        print(f"{self.animal2} is also pet.")

# create a obj

Pet = Animal()
print(Pet.animal1 , Pet.animal2)

Pet.Dog()
