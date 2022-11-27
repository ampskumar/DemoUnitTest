class OurClass:
    def __init__(self):
        pass

    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        print('class method called')
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        print('static method called')
        return 'static method called'


# obj = OurClass()
# obj.staticmethod()
# OurClass.classmethod()
# obj.method()


class Calculator:
    # @staticmethod
    def addNumbers(x, y):
        return x + y
# create addNumbers static method
# Calculator.addNumbers = staticmethod(Calculator.addNumbers)
print('Product:', Calculator.addNumbers(15, 110))


class Person:
    name = ""
    age = 0
    count = 0

    def __init__(self, person_name, person_age):
        print("self.name", self.name)
        self.name = person_name
        self.age = person_age
        self.count += 1

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)

    @classmethod
    def show_count(cls):
        cls.count = self.count
        print(count)


# Create an object of the class
person1 = Person("John", 23)
#Create another object of the same class
person2 = Person("Anne", 102)
#call member methods of the objects
person1.show_age()
person2.show_name()
print(person2.count)
# print(Person.count)
