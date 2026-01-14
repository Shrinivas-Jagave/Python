'''
Author : Shrinivas Umakant Jagave
Question : Remove duplicates from a list.

'''
def RemoveDuplicates(L:list)->list:
    if not isinstance(L, list):
        raise TypeError("Invalid Type..")
    if not L:
        raise ValueError("List Should not empty")

    return list(dict.fromkeys(L))

def main():
    L = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
    print(RemoveDuplicates(L))

main()
