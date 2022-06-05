'''
                                  12.Constructors
1. Write a class with a default constructor, one argument constructor and two argument
constructors. Instantiate the class to call all the constructors of that class from a main
class
2. Call the constructors(both default and argument constructors) of super class from a child
class
3. Apply private, public, protected and default access modifiers to the constructor
4. Write a program which illustrates the concept of attributes of a constructor.
'''

# from unicodedata import name

class A:
    # Default Constructor
    def __init__(self):
        self.name = "NARUTO"
    def print_A(self):
        print(self.name)
obj = A()
# print(obj)
obj.print_A()

class B(A):
    def __init__(self):
        self.name = "HINATA"
    def print_B(self):
        print(self.name)
obj1 = B()
obj1.print_B()

class C:
    name = None
    _roll = None
    _branch = None

    # Constructor
    def __init__(self, name, roll, branch):
        self.name = name
        self._roll = roll
        self._branch = branch
    def displayName(self):
        print("Name : ", self.name)
    def _displayRoll(self):
        print("Roll : ", self._roll)
    def _displayBranch(self):
        print("Branch : ", self._branch)
    def access_displayBranch(self):
        self._displayBranch()

class D(C):
    def __init__(self, name, roll, branch):
        super().__init__(name, roll, branch)
    def access_displayRoll(self):
        self.access_displayBranch()

obj = D("NARUTO", 5, "CSE")
obj.displayName()
obj.access_displayRoll()
obj.access_displayBranch()