'''
                                8.Access Modifiers
1. Create a class with PRIVATE fields, private method and a main method. Print the fields
in main method. Call the private method in main method.
Create a sub class and try to access the private fields and methods from sub class.

2. Create a class with PROTECTED fields and methods. Access these fields and methods
from any other class in the same package.
Also, Access the PROTECTED fields and methods from child class located in a different
package
Access the PROTECTED fields and methods from any class in different package

3. Create a class with PUBLIC fields and methods.
Access the public methods and fields from any class in the same package or different
package.
'''

class Super():
    var1 = None    # Public data member
    _var2 = None   # Protected data member
    _var3 = None   # Private data member

    #  Constructor
    def __int__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self._var3 = var3

    #   Public Member Function
    def displayPublicMembers(self):
        print("Public Data Member: ", self.var1)

    #   Proteceted Member Function
    def _displayProtectedMembers(self):
        print("Proteceted Data Member: ", self._var2)

    #   Private Member Function
    def _displayPrivateMembers(self):
        print("Private Data Member: ", self._var3)

    # Public member Functions
    def accessPrivateMembers(self):
        self._displayPrivateMembers()

# Derived Class
class Sub(Super):
    # Constructor
    def __init__(self, var1, var2, var3):
        Super.__int__(self, var1, var2, var3)

    #   Public member function
    def accessProtectedMembers(self):
        self._displayProtectedMembers()

obj = Sub("KG", 5, "KG !")

obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()













