'''
                    6.Strings
1. Different ways creating a string
2. Concatenating two strings using + operator
3. Finding the length of the string
4. Extract a string using Substring
5. Searching in strings using index()
6. Matching a String Against a Regular Expression With matches()
7. Comparing strings
8. startsWith(), endsWith() and compareTo()
9. Trimming strings with strip()
10. Replacing characters in strings with replace()
11. Splitting strings with split()
12. Converting integer objects to Strings
13. Converting to uppercase and lowercase
'''


# 1. Different ways creating a string
string = 'Hello'
print(string)

string1 = "Hello"
print(string1)

string2 = '''Hello'''
print(string2)

string3 = """Wake up
            to the
            reality."""
print(string3)

# 2. Concatenating two strings using + operator
str1 = "Wake up to the reality "
str2 = " Nothing will go as ever planned."
strn = str1 + str2
print(strn)

# 3. Finding the length of the string
print("\n Length of the string is: ", len(str2))
print()

# 4. Extract a string using Substring -> string[start: end: step]
print(str1[14: -1: 1])

# 5. Searching in strings using index()
str3 = 'kakashi'
str1 = 'ashi'
str2 = 'k'
print('Position of ashi: ', str3.index(str1))
print('Position of k: ', str3.index(str2))
print()

# 6. Matching a String Against a Regular Expression With matches()
import re
Substr = 'Uchiha Madara'
str6 = 'Uchiha Madara once said- Wake up to relity nothing goes as planned in this cursed world'
print(re.match(Substr, str6))
print()

# 7. Comparing strings
str8 = 'Itachi Uchiha'
str2 = 'Madara Uchiha'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 == str1)
print()

# 8. startsWith(), endsWith() and compareTo()
string  = 'Minato Namikaze'
print(string.startswith("Minato"))
print(string.endswith("kaze"))
print()

# 9. Trimming strings with strip()
str7 = "Hello World hi"
print(str7.strip("hi"))

# 10. Replacing characters in strings with replace()
string = 'Hi World'
print(string.replace('Hi', 'Hello'))
print()

# 11. Splitting strings with split()
str9 = 'hi-hello-bye'
print(str9.split('-'))
print()

# 12. Converting integer objects to Strings
num = 10
num1 = str(num)
print(num1)
print(type(num1))
print()

# 13. Converting to uppercase and lowercase
string = 'hello'
string1 = "WORLD"
print(string.upper())
print(string1.lower())














































































































































