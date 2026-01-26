'''
Author : Shrinivas Umakant Jagave
Question : Find common elements in two lists

'''
def CommonElements(List1:list, List2:list)->list:
    if not isinstance(List1, list) or not isinstance(List2, list):
        raise TypeError("Type Error")
    
    if not List1 or not List2:
        raise ValueError("List Should not empty")
    
    common = set(List1).intersection(set(List2))

    return list(common)

def main():
    List1 = [1, 2, 3, 4, 5, 43, 2, 1]
    List2 = [3, 5, 9, 0, 8, 7, 3, 1]

    print("Comman Elements are : ", CommonElements(List1, List2))

main()
