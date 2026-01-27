'''
Author : Shrinivas Umakant Jagave
Question : Check if list is sorted

'''
def CheckIfListIsSorted(L:list)->bool:
    if not isinstance(L, list):
        raise TypeError("Type Error")
    
    if not L:
        raise ValueError("List Should not empty")
    
    return L == sorted(L)

def main():
    L = [1, 2, 3, 4, 5, 1, 44]

    if CheckIfListIsSorted(L) == True:
        print("List IS Sorted")
    else:
        print("List Is Not Sorted")

main()
