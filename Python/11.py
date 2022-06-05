'''
                            11.FILES
1. Write a program to read text file
2. Write a program to write text to .txt file using InputStream
3. Write a program to read a file stream
4. Write a program to read a file stream supports random access
5. Write a program to read a file a just to a particular index using seek()
6. Write a program to check whether a file is having read access and write access permissions
'''

# 1. Write a program to read text file
import errno
import io, os, stat, linecache

file1 = open("Tanveer.txt", "r")
data = file1.read()
print(data)
print()

# 2. Write a program to write text to .txt file using InputStream
file2 = open("Blank.txt", "w")
Str1 = "WELCOME TO JALA ACADEMY"
file2.write(Str1)
print()

# 3. Write a program to read a file stream
file3 = open("Tanveer.txt", "r+")
print(file3.readlines(1))
print()

# 4. Write a program to read a file stream supports random access
# f = open("Blank.txt", "r", encoding="utf-8")
# f = io.StringIO("some initial text data")
# print(f)
print(linecache.getline('Blanks.txt', 5))

# 5.Write a program to read a file a just to a particular index using seek()
f = open("Blanks.txt", "r")
f.seek(10)
print(f.tell())
print(f.readlines())
f.close()

# 6. Write a program to check whether a file is having read access and write access permissions
def isgroupreadable(filepath):
  st = os.stat(filepath)
  return bool(st.st_mode & stat.S_IRGRP)

isgroupreadable("Blanks.txt")
