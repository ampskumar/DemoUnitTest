# Python program to demonstrate
# use of a class method and static method.
"""
It can modify a class state that would apply across all the instances of the class.
For example, it can modify a class variable that would be applicable to all the instances.
"""
from datetime import date


class Person:
    base_price = 1000

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a
    # Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @classmethod
    def revise_base_method(cls, change_base_price):
        cls.base_price = change_base_price

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person3= Person('maya', 20)
person1.base_price=2000
print(person1.base_price)
person3.base_price=5000
print(person3.base_price)
print(Person.base_price)
print(".........latest......")
# Person.base_price=3000
Person.revise_base_method(3000)
print(person1.base_price)
print(person3.base_price)
print(Person.base_price)
# person2 = Person.fromBirthYear('mayank', 1996)
# print(person1.age)
# print(person2.age)
# print(Person.isAdult(22))
