import sqlite3
import timeit

class Product:
    def __init__(self, name="", country="", volume=-1, price=-1.0):
        self.name = name
        self.country = country
        self.volume = volume
        self.price = price

    def __gt__(self, other):
        if self.name > other.name:
            return True
        elif self.name < other.name:
            return False
        if self.volume > other.volume:
            return True
        elif self.volume < other.volume:
            return False
        if self.country > self.country:
            return True
        elif self.country < self.country:
            return False

        return True

    def __eq__(self, other):
        return self.name == other.name and self.volume == other.volume and self.country == other.country

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return self == other or self < other

    def __ge__(self, other):
        return self == other or self > other

    def __repr__(self):
        return self.name + " " + self.country + " " + str(self.volume) + " " + str(self.price)

