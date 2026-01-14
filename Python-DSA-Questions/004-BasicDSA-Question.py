'''
Author : Shrinivas Umakant Jagave
Question : Count the number of even and odd numbers in a list.

'''

def CountEvenOdd(L:list)->None:
    if not isinstance(L, list):
        raise TypeError("Invalid Type")
    
    if not L:
        raise ValueError("List Should Not Empty")

    even = 0
    odd = 0

    for element in L:
        if not isinstance(element, int):
            raise TypeError("List must contain only integers")
        if element % 2 == 0:
            even = even + 1
        if element % 2 != 0:
            odd = odd + 1 

    print(f"Even : {even}")
    print(f"Odd : {odd}")


def main():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    CountEvenOdd(L)

main()
