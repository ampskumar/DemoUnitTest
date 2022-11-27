class Parent(object):
    pass


class Child(Parent):
    pass


# Driver Code
print(issubclass(Child, Parent))  # True
print(issubclass(Parent, Child))  # False

# We can check if an object is an instance of a class by making use of isinstance() method:
obj1 = Child()
obj2 = Parent()
print(isinstance(obj2, Child))    #False
print(isinstance(obj2, Parent))   #True
