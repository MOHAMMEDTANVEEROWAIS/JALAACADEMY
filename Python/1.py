'''
                            1.Python Basics
1. Write a program to print your name.
2. Write a program for a Single line comment and multi-line comments
3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables
'''

# 1. Write a program to print your name
print("Mohammed Tanveer Owais.\n")

# 2. Write a program for a Single line comment and multi-line comments
print("# This is a SINGLE LINE COMMENT \n")

print("'''This is multi line comment \n Myself Mohammed Tanveer Owais. \n I am from hyderabad ''' \n")

# 3. Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
# a = -8
a = +12
# a = 0
print("Type of a : ", type(a),  "\n")

b = True
# b = False
print("Type of a : ", type(b),  "\n")

# a = 12.0 # a = 0.0
c = +12.0
print("Type of a : ", type(c),  "\n")

string  = "JALA ACADEMY"
print("Type of a : ", type(string),  "\n")

# Character in Python
print(chr(74),chr(65),chr(76),chr(65), ' ', chr(65),chr(67),chr(65),chr(68),chr(69),chr(77),chr(89), "\n")

# 4. Define the local and Global variables with the same name and print both variables and understand the scope of the variables

a = 10
# Uses global because there is no local 'a'
def me():
    print('Inside me() : ', a)
# Variable 'a' is redefined as a local
def you():
    a = 5
    print('Inside you() : ', a)
# Uses global keyword to modify global 'a'
def other():
    global a
    a = 1      #Value of 'a' modified
    print('Inside other() : ', a)

# Global scope
print('global : ', a)
me()
print('global : ', a)
you()
print('global : ', a)
other()
print('global : ', a)





