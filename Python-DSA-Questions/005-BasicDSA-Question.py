'''
Author : Shrinivas Umakant Jagave
Question : Reverse a list.

'''

def ReverseList(L:list)->list:
    if not isinstance(L, list):
        raise TypeError("Invalid Type")
    
    if not L:
        raise ValueError("List Should Not Empty")
    
    return L[::-1]

def main():
    L = [0, 1, 2, 3, 4, 5, 6]

    print(ReverseList(L))

main()