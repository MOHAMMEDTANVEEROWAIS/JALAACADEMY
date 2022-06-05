'''
                                4.Arrays
1. Write a function to add integer values of an array
2. Write a function to calculate the average value of an array of integers
3. Write a program to find the index of an array element
4. Write a function to test if array contains a specific value
5. Write a function to remove a specific element from an array
6. Write a function to copy an array to another array
7. Write a function to insert an element at a specific position in the array
8. Write a function to find the minimum and maximum value of an array
9. Write a function to reverse an array of integer values
10. Write a function to find the duplicate values of an array
11. Write a program to find the common values between two arrays
12. Write a method to remove duplicate elements from an array
13. Write a method to find the second largest number in an array
14. Write a method to find the third largest number in an array
15. Write a method to find number of even number and odd numbers in an array
16. Write a function to get the difference of largest and smallest value
17. Write a method to verify if the array contains two specified elements(12,23)
18. Write a program to remove the duplicate elements and return the new array
'''

# 1. Write a function to add integer values of an array
arr = [10,20,30,40,50]
sum = 0
for i in range(0, len(arr)):
    sum = sum + arr[i]
print('Sum of all integers values in array is : ', sum)


# 2. Write a function to calculate the average value of an array of integers
def average(num):
    sum_num = 0
    for i in num:
        sum_num = sum_num + i

    avg = sum_num / len(num)
    return avg

print("The average is", average([10,21,32,43,54]))


# 3. Write a program to find the index of an array element
arr = [1,3,5,3,1,2,6,5,3,8,6,9]
index= arr.index(3)
print('Index of 3: ', index)

index= arr.index(5)
print('Index of 3: ', index)

index= arr.index(8)
print('Index of 3: ', index)


# 4. Write a function to test if array contains a specific value
arr = [4,5,45,40,50]
for num in arr:
    if num == 5:
        print("Element Exist")
print("The element does not exist.")

# 5. Write a function to remove a specific element from an array
arr = [44,55,0,15,19,5,4]
arr.remove(0)
print(arr)

# 6. Write a function to copy an array to another array
arr = ['T', 'a', 'n', 'v', 'e', 'e', 'r']
arr1 = []
arr1 = arr.copy()
print(arr1)

# 7. Write a function to insert an element at a specific position in the array
arr = [101,303,404,505,606,707,808,909]
arr.insert(1, 202)
print(arr)

# 8. Write a function to find the minimum and maximum value of an array
arr = [20, 10, 3, 56, 78 ,92 ,45, 67, 99]
minValue = min(arr)
print(minValue)
maxValue = max(arr)
print(maxValue)

# 9. Write a function to reverse an array of integer values
arr = [10,9,8,7,6,5,4,3,2,1]
arr.reverse()
print(arr)

# 10. Write a function to find the duplicate values of an array
arr = [21,11,31,13,11,31]
for i in range(0, len(arr)):
    for k in range(i+1, len(arr)):
        if arr[i] == arr[k]:
            print('Duplicate element in the given array are: ', arr[k])

# 11. Write a program to find the common values between two arrays
arr = ['T', 'a', 'n', 'v', 'e', 'e', 'r']
arr1 = ['a', 'b', 'd', 'e']
arr2 = list(set(arr) & set(arr1))
print('Common values in given array are: ', arr2)

# 12. Write a method to remove duplicate elements from an array
arr = [21,11,31,13,11]
finalarr = []
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)


# 13. Write a method to find the second largest number in an array
arr = [100, 88, 45, 67, 89, 94, 64, 99, 105]
arr.sort()
print("Second Largest interger is: ", arr[-2])

# 14. Write a method to find the third largest number in an array
arr = [100, 88, 45, 67, 89, 94, 64, 99, 105]
arr.sort()
print("Third Largest interger is: ", arr[-3])


# 15. Write a method to find number of even number and odd numbers in an array

arr = [0,1,2,3,4,5,6,7,8,9.10]
evennumbers = 0
oddnumbers = 0
for i in arr:
    if i%2 == 0:
        evennumbers += 1
    else:
        oddnumbers += 1
print("EvenNumbers in given array is: ", evennumbers)
print("OddNumbers in given array is: ", oddnumbers)

# 16. Write a function to get the difference of largest and smallest value
arr = [10,6,11,13,14]
arr.sort()
print("Difference of largest and smalllest value is : ", arr[4]-arr[0])

# 17. Write a method to verify if the array contains two specified elements(12,23)
arr = [1,12,19,23,33,54,11]
for i in arr:
    if i == 12 :
        print("Exist in array")
    if i == 23:
        print("Exist in array")

# 18. Write a program to remove the duplicate elements and return the new array
a = [11,22,33,44,55,22,55]
f = []
for i in a:
    if i not in f:
        f.append(i)
print(f)






















































































































