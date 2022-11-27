# https://www.scaler.com/topics/super-in-python/

# The super() function has two major use cases:
#
# To avoid the usage of the super (parent) class explicitly.
# To enable multiple inheritances ​.

# Parent Class
class Vehicle:
    def __init__(self, company, model, year, color):
        self.company = company
        self.model = model
        self.year = year
        self.color = color


#
#
# Child Class
class Car(Vehicle):
    def __init__(self, company, model, year, color, car_type):
        # Using super to access __init__ method of Parent Class
        super().__init__(company, model, year, color)
        self.car_type = car_type


# Creating an object of Car
my_car = Car("Tesla", "S", 2021, "Silver", "Sedan")
print(f"I have a {my_car.company} model {my_car.model}.")

print("-----ex 2---------")
#
#
# class Animal:
#     def smell(self, name):
#         print(name, "can smell")
#
#
# class Dog(Animal):
#     def __init__(self):
#         super().smell("Dog")
#
#     def bark(self):
#         print("Dog can bark")
#
#
# dog = Dog()
# dog.bark()
#

# # print("------super() with Multiple Inheritance------")
#
#
# class Parent:
#     def __init__(self):
#         print("This is the parent class")
#
#
# class Parent1:
#     def __init__(self):
#         print("This is the parent1 class")
#
#
# class Child(Parent1, Parent):
#     def __init__(self):
#         # Calling constructor of the Parnet 1 class
#         super().__init__()
#
#
# ob = Child()

print("---mro childs super call to multiple classes---")


# Let's understand how to access the constructor of the Parent class from the Child class.


class Parent:
    def __init__(self):
        print("This is the parent class")


class Parent1:
    def __init__(self):
        print("This is the parent1 class")


class Child(Parent1, Parent):
    def __init__(self):
        # Calling constructor of the Parent 1 class
        super(Parent1, self).__init__()


ob = Child()

# print(Child.mro())
# o/p : [<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent'>, <class 'object'>]


d = {"keys":[]}