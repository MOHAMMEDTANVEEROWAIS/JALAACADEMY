'''
                          14.Exceptions
1. Write a program to generate Arithmetic Exception without exception handling
2. Handle the Arithmetic exception using try-catch block
3. Write a method which throws exception, Call that method in main class without try block
4. Write a program with multiple catch blocks
5. Write a program to throw exception with your own message
6. Write a program to create your own exception
7. Write a program with finally block
8. Write a program to generate Arithmetic Exception
9. Write a program to generate FileNotFoundException
10. Write a program to generate ClassNotFoundException
11. Write a program to generate IOException
12. Write a program to generate NoSuchFieldException
'''

# 1. Write a program to generate Arithmetic Exception without exception handling
a = [1,2,3]
try:
    print("Second element = ", a[1])
    print("Fourth element = ", a[3])
except:
    print("An error Occured.")

# 2. Handle the Arithmetic exception using try-catch block
b = [3,2,1]
try:
    a == b
except:
    print("They are not equal.")
else:
    print("Both Equal.")

# 3. Write a method which throws exception, Call that method in main class without try block
try:
    k = 5/10
    print(k)
except ZeroDivisionError:
    print("Can't divide by ZERO")
finally:
    print("This is always executed.")

# 4. Write a program with multiple catch blocks
try:
    name = "Owais"
    name += 5
except NameError as ne:
    print(ne)
except TypeError as te:
    print(te)

# 5. Write a program to throw exception with your own message
class MyException(Exception):
        pass
try:
    raise MyException({"Message" : "My hovercraft is full of animals", "animal" : "eels"})
except MyException as e:
    details = e.args[0]
    print(details["animal"])

# 6. Write a program to create your own exception
class SalaryNotInRangeError(Exception):

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)

# 7. Write a program with finally block
try:
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    print("Result of Division: " + str(a / b))
# except block handling division by zero
except(ZeroDivisionError):
    print("You have divided a number by zero, which is not allowed.")
finally:
    print("Code execution Wrap up!")
# outside the try-except block
print("Will this get printed?")

# 8. Write a program to generate Arithmetic Exception
try:
    a = 10/0
    print(a)
except ArithmeticError:
    print("This statement is raising an arithmetic exception.")
else:
    print("SUCCESS!")

# 9. Write a program to generate FileNotFoundException
# trying to open a file, which does not exist
try:
    #trying to open a file in read mode
    fo = open("Blanks.txt","rt")
    print("File opened")
except FileNotFoundError:
    print("File does not exist")
except:
    print("Other error")

# 10. Write a program to generate ClassNotFoundException
a = input("Enter Class Name to find: ")
class python():
    def __init__(self, namw):
        self.name = 'UZUMAKI NARUTO'
    def PrintName(self):
        print("My Name is : ", self.name)
obj = python("NARUTO")
obj.PrintName()
try:
    if a == True:
        print("CLASS FOUND!")
except FileExistsError as CNFE:
    print("Class Not Found")

# 11. Write a program to generate IOException

try:
    f = open ( "foo.txt", 'r' )
except IOError as e:
    print(e)

# 12. Write a program to generate NoSuchFieldException
filename = 'John.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file "+ filename + "does not exist."
    print(msg)