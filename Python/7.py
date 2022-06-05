'''
                                7. Inheritance
A, B and C are classes
A is a super class. B is a sub class of A. C is a sub class of B.
Create three methods in each class, 2 methods are specific to each class and third
method (override method) should be in all three Classes A, B and C
Create a class with main method. Create an object for each class A, B and C in main
method and call every method of each class using its own object/instance.
Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above
process only for data members
'''

class A():
    def display(dp):
        print("Display inside CLASS A")

    def show(self):
        print("Show inside CLASS A")

class B(A):
    def display(pt):
        print("Display inside CLASS B")

    def show(self):
        print("Show inside CLASS B")

class C(A):
    def show(self):
        print("Show Inside CLASS C")

s = A()
s.display()
k = B()
print(k)
g = C()
g.show()