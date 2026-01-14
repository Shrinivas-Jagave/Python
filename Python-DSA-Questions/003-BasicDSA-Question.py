'''
Author : Shrinivas Umakant Jagave
Question : Find the sum of all elements in a list.

'''

def SumOfAllElementInList(L:list)->float:
    if not isinstance(L, list):
        raise TypeError("Invalid Type")
    
    if not L:
        raise ValueError("List Should Not Empty")
    
    result = 0
    for element in L:
        if not isinstance(element, (int, float)):
            raise TypeError("List must contain only integers and floating value")
        
        result += element

    return result

def main():
    L = [0, 1, 2, 3, 4.5, 5.5, 6]

    print(SumOfAllElementInList(L))

main()