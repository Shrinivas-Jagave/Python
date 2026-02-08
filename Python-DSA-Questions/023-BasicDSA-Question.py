'''
Author : Shrinivas Umakant Jagave
Question : Find duplicate elements in a list.
'''

def DuplicateElementsINList(L: list) -> dict:
    if not isinstance(L, list):
        raise TypeError("Input must be a list")

    duplicate_dict = {}

    for element in L:
        duplicate_dict[element] = duplicate_dict.get(element, 0) + 1

    result = {}
    for key, value in duplicate_dict.items():
        if value > 1:
            result[key] = value

    return result

def main():
    L = [1, 2, 3, 4, 5, 6, 2, 3, 4, 1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 2, 6, 7, 8, 9, 6]

    print(DuplicateElementsINList(L))

main()
