'''
                        2.Operators
1. Write a function for arithmetic operators(+,-,*,/)
2. Write a method for increment and decrement operators(++, --)
3. Write a program to find the two numbers equal or not.
4. Program for relational operators (<,<==, >, >==)
5. Print the smaller and larger number
'''

# 1. Write a function for arithmetic operators(+,-,*,/)

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)
sub = float(num1) - float(num2)
mul = float(num1) * float(num2)
div = float(num1) / float(num2)

print('The Addition of {0} and {1} is {2}.'.format(num1, num2, sum)) #or
# print(f'The Addition of {num1} and {num2} is {sum}.')
print('The Subraction of {0} and {1} is {2}.'.format(num1, num2, sub)) #or
# print(f'The Subraction of {num1} and {num2} is {sub}.')
print('The Multiplication of {0} and {1} is {2}.'.format(num1, num2, mul)) #or
# print(f'The Multiplication of {num1} and {num2} is {mul}.')
print('The Division of {0} and {1} is {2}.'.format(num1, num2, div)) #or
# print(f'The Division of {num1} and {num2} is {div}.')


# 2. Write a method for increment and decrement operators(++, --)

a = 0
a += 1
a = a+1
print('The value of a is : ', a)

print("Incremented For Loop")
for i in range(0, 5):
    print(i)

print("Decremented For Loop")
for i in range(4, -1, -1):
    print(i)

# 3. Write a program to find the two numbers equal or not.

a = input('Enter first number: ')
b = input('Enter second number: ')

if a==b:
    # print(f'{a} is equal to {b}') #or
    print('Both numbers are equal')
else:
    print('Both numbers are not equal')


# 4. Program for relational operators (<,<==, >, >==)

a = 5
b = 4
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)


# 5. Print the smaller and larger number

a = float(input('Enter first number : '))
b = float(input('Enter second number : '))

'''if a>b:
    print(a, ' is greater')
elif b>a:
    print(b, ' is greater')
else:
    print('Both numbers are equal')'''

if a > b:
     print(a, "is greater ")
else:
    print(b, " is greater ")
if a < b:
     print(a, "is smaller2 ")
else:
    print(b, " is smaller ")






































