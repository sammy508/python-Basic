
# Abstract Property in pytohn

import abc
from abc import ABC, abstractmethod

class paernt (ABC):
    @abc.abstractmethod
    def geeks(self):
        return "paernt class"
    

class child(paernt):
    @property

    def geeks(self):
        return "Child class"
try:
    r = paernt()
    r.geeks()
except Exception as error:
    print(error)

t = child()
t.geeks()

