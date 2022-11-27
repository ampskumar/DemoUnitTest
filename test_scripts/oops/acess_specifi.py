# to demonstrate access specifiers
class InterviewbitEmployee:
    # protected members
    _emp_name = None
    _age = None

    # private members
    __branch = None

    # constructor
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch

    # public member
    def display(self):
        print(self._emp_name + " " + str(self._age) + " " + self.__branch)


# a = InterviewbitEmployee('amit', 30, 'cs')
# a.display()


class Child(InterviewbitEmployee):
    def __init__(self):
        print("in child init")
        super().__init__('amit', 30, 'cs')
        # self.age = 30


c = Child()
c.display()     # amit 30 cs