'''
                                3.Loops
1. Write a program to print “Bright IT Career” ten times using for loop
2. Write a program to print 1 to 20 numbers using the while loop.
3. Program to equal operator and not equal operators
4. Write a program to print the odd and even numbers.
5. Write a program to print largest number among three numbers.
6. Write a program to print even number between 10 and 20 using while
7. Write a program to print 1 to 10 using the do-while loop statement.
8. Write a program to find Armstrong number or not
9. Write a program to find the prime or not.
10. Write a program to palindrome or not.
11. Program to check whether a number is EVEN or ODD using switch
12. Print gender (Male/Female) program according to given M/F using switch
'''

# 1. Write a program to print “Bright IT Career” ten times using for loop
a = "Bright IT Career"
for i in range(10):
    print(a)

# 2. Write a  program to print 1 to 20 numbers using the while loop.

i = 1
while(i<21):
    print(i)
    i+=1

# 3. Program to equal operator and not equal operators
a = 6
b = 7
print(a==b)
print(a!=b)

# 4. Write a program to print the odd and even numbers.
Numbers = [1,2,3,4,5,6,7,8,9,10]
print('Even Numbers are :  ')
for i in Numbers:
    if i%2 == 0:
        print(i, end=" ")

print('\n Odd Numbers are :  ')
for i in Numbers:
    if i%2 != 0:
        print(i, end=" ")
print()

# 5.Write a program to print largest number among three numbers.

l = 10
m = 20
n = 30

if l >= m and l >= n:
    print('Largest number is : ', l)  #Largest = l
elif m >= l and m >= n:
    print('Largest number is : ', m) #Largest = m
else:
    print('Largest number is : ', n) #Largest = n
# print("Largest number is : ", Largest)

# 6. Write a program to print even number between 10 and 20 using while loop
j = 10
k = 20
print("Even Numbers Between 10 to 20 : ", end=" ")
while j <= k:
    if (j % 2  == 0):
        # print("{0}".format(j),end=" ")
#         or
        print(f'{j}', end=" ")
    j = j+1
print()


# 7. Write a program to print 1 to 10 using the do-while loop statement.
a = 1
print('Print 1 to 10 using the do-while loop statement:', end=" ")
while True:
    print(a, end=" ")
    a += 1
    if (a>10):
        break
print()


# 8. Write a program to find Armstrong number or not

a = int(input('Enter a number to check if its armstrong number or not : '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r**3
    temp //= 10
if a == sum:
    print(a, ' is an armstrong number')
else:
    print(a, ' is not an armstrong number')


# 9. Write a program to find the prime or not.

number = int(input("Enter any number to check given number is prime or not:"))

if number>1:
    for i in range(2, number):
        if (number % i ) == 0:
            print(number, " is not a Prime Number.")
            break
    else:
        print(number, ' is a Prime Number.')
else:
    print(number, ' is not a Prime Number.')


# 10. Write a program to palindrome or not.

n = int(input("Enter number to check given number is Palindrome or not:"))
temp = n
rev = 0
while(n>0):
    pal = n%10
    rev = rev*10 + pal
    n = n//10
if (temp == rev):
    print("The number is a Palindrome.")
else:
    print("The number isn't a Palindrome.")


# 11. Program to check whether a number is EVEN or ODD using switch

a = int(input("Enter a number to check is EVEN or ODD : "))
if (a%2 == 0):
    print(f'{a} is EVEN NUMBER.')
else:
    print(f'{a} is an ODD NUMBER.')

# 12. Print gender (Male/Female) program according to given M/F using switch

def define_gender(gender):
    gender_class = {
        'M' : "Male",
        'm' : "Male",
        'F' : "Female",
        'f' : "Female"
    }
    return gender_class.get(gender, 'Invalid Option')
gender = str(input("Enter your gender as M/m/F/f: "))
print(define_gender(gender))
































































































































