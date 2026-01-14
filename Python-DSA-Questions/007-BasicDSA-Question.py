'''
Author : Shrinivas Umakant Jagave
Question : Find the second largest element in a list.

'''

def SecondLargestElement(L:list)->int:
    if not isinstance(L, list):
        raise TypeError("Invalid Type")
    
    if not L:
        raise ValueError("List should not empty")
    
    NonDuplicateList = sorted(list(dict.fromkeys(L)))

    return NonDuplicateList[len(NonDuplicateList) - 2]

def main():
    L = [48, 1, 2, 3, 4, 5, 6, 7, 7, 7]
    print(SecondLargestElement(L))

main()
