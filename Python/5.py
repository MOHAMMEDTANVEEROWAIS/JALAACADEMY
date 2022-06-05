'''
                            5.Static
1. Define a static variable and access that through a class
2. Define a static variable and access that through a instance
3. Define a static variable and change within the instance
4. Define a static variable and change within the class
'''

# 1. Define a static variable and access that through a class
class Python:
    staticVariable = 9
print(Python.staticVariable)

# 2.access that through a instance
instance = Python()
print(instance.staticVariable)

# 3.change within the instance
instance.staticVariable = 15
print(instance.staticVariable)


# 4. change within the class
Python.staticVariable = 12
print(Python.staticVariable)

# # 3.change within the instance
# instance.staticVariable = 15
# print(instance.staticVariable)
# print(Python.staticVariable)

























































































































































