
class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.last_name = last

    @classmethod
    def add_salary(cls, salary):
        cls.mysalary = salary


p1 = Person("srk", "patil")

p1.add_salary(10000)
print(p1.mysalary)
print(Person("sr", "pat").add_salary(500000))
p2 = Person("sr", "pat")
p2.add_salary(500000)
print(p2.mysalary)
print(p1.mysalary)