

# Polymorphism with class

class Nepal(object):

    def capital(self):
        return ("Capital of nepal is Ktm ")

    def Lang(self):
        return ("Main lang is Nepali")

class Usa(object):
    def capital(self):
        return ("Capital of nepal is Washington")

    def Lang(self):
        return ("Main lang is Eng")


obj1 = Nepal()
obj2 = Usa()
for country in (obj1 , obj2):
    print(country.capital())
    print(country.Lang())
