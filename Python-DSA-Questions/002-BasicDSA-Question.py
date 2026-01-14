'''
Author : Shrinivas Umakant Jagave
Question : Find the minimum element in a List.

'''

def MinimumElementInList(L:list)->int:
    if not isinstance(L, list):
        raise TypeError("Invalid Type")
    
    if not L:
        raise ValueError("List Should Not Empty")
    
    return min(L)

def main():
    L = [0, 1, 2, 3, 4, 5, 6]

    print(MinimumElementInList(L))

main()