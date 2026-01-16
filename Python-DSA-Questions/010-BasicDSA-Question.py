'''
Author : Shrinivas Umakant Jagave
Question : Find the largest of three numbers

'''

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    print(largest_of_three(10, 25, 15))

main()
