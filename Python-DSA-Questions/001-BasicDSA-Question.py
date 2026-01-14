'''
Author : Shrinivas Umakant Jagave
Question : Find the maximum element in a List.

'''

def MaximumElementInList(L:list)->int:
    if not isinstance(L, list):
        raise TypeError("Invalid Type")
    
    if not L:
        raise ValueError("List Should Not Empty")
    
    return max(L)

def main():
    L = [0, 1, 2, 3, 4, 5, 6]

    print(MaximumElementInList(L))

main()
