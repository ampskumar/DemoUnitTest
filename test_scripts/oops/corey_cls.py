class Employee:
    raise_amount = 1
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@slg.com'
        # self.num_of_emps += 1 #  o/p:0
        Employee.num_of_emps += 1  # o/p:2

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Employee('Amit', 'Patil', '50000')
emp2 = Employee('Amit', 'Patil', '60000')
full_name = emp1.fullname()  # Employee.fullname(emp1)
print(full_name)

#  global variable can be accessed only by using classname or object name
raised_amount = emp1.apply_raise()  # Employee.raise_amount
print("amount raised by emp1 is : ", raised_amount)

print("printing emp1 r_amt before", emp1.raise_amount)

Employee.raise_amount = 1.05
print("printing emp1 r_amt after Emp", emp1.raise_amount)

emp1.raise_amount = 2.05
print("Emp : ", Employee.raise_amount)
print("emp1 : ", emp1.raise_amount)

Employee.raise_amount = 3.05
print("Emp : ", Employee.raise_amount)
print("emp1 : ", emp1.raise_amount)

print("Total employess : ", Employee.num_of_emps)

Employee.set_raise_amount(7.7)
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
# It does not contain global variable
# print(emp1.__dict__)

# it will have global variable
# print(Employee.__dict__)
