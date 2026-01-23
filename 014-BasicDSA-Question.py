'''
Author : Shrinivas Umakant Jagave
Question : Reverse a string without using built-in functions

'''

s = "hello"
rev = ""

for i in range(len(s) - 1, -1, -1):
    rev += s[i]

print("Reversed string:", rev)
