'''
                            15.Dictionary
1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
    1.1. Adding the values in dictionary
    1.2. Updating the values in dictionary
    1.3. Accessing the value in dictionary
    1.4. Create a nested loop dictionary
    1.5. Access the values of nested loop dictionary
    1.6. Print the keys present in a particular dictionary
    1.7. Delete a value from a dictionary
'''
Dict = dict([
    (1, 'Minato'), (2, 'Kakashi'), (3, 'Might Guy'), (4, 'Naruto'), (5, 'Boruto')]
)
print(Dict)

Dict[6] = 'Obito'
print("\n Dictionary with new Item added: ", Dict)

Dict[3] = 'Hinata'
print("\n Dictionary with Updated Values : ", Dict)

print("\n Accessing thedictionary : ", Dict[1])

del Dict[6]
print("\n Delete a value from a Dictionary : ", Dict)

Dict1 = {1: 'OWAIS', 2: 'AMEER',
        3:{'Age' : 20, 'Branch' : 'CSE', 'Year' : 'Third Year'}}
print("\n Nested loop Dictionary:",Dict1)

print("\n Accessing an element of a Nested Dictionary:",Dict1[2])

print("\n Accessing key element of a Dictionary:",Dict.keys())
print("\n Accessing Values  of a Dictionary:",Dict.values())
print(Dict.get(1))