

# Abstract classes in python

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod

    def noofside(self):
        pass

class triangle(Polygon):

    def noofside(self):
        print("Have 3 sides")

class penta(Polygon):

    def noofside(self):
        print("Have 5 sides")

T= triangle()
T.noofside()

P = penta()
P.noofside()