class Employee:
    raise_amount = 1
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@slg.com'
        # self.num_of_emps += 1 #  o/p:0
        Employee.num_of_emps += 1  # o/p:2

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        return cls.raise_amount


emp1 = Employee('Amit', 'Patil', '50000')
emp2 = Employee('Amit', 'Patil', '60000')

# emp1.raise_amount = 2.05  # checkout this commenting and uncommenting
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

"""from the above output it is evident that 
1)if the member of a class is not changed explicitly by an object 
   then its value will be same as claas_name.member,
2)if the member of a class is explicitly overidden by an object 
   then its value will not be same as claas_name.member
"""

emp1.set_raise_amount(13.5)
print("emp1 is accesing global var by class method")
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)