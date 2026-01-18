'''
Author : Shrinivas Umakant Jagave
Question : Find Occurrences of each element in a list
'''

def Occurrences(L: list) -> None:
    if not isinstance(L, list):
        raise TypeError("Type Error")
    
    if not L:
        raise ValueError("List should not be empty")

    Dict = {}

    for e in L:
        Dict[e] = Dict.get(e, 0) + 1

    for key, value in Dict.items():
        print(f"{key} : {value}")

def main():
    L = [1, 2, 3, 1, 2, 3, 44, 33, 33, 44, 1, 2, 66, 7, 66, 9]
    Occurrences(L)

main()
