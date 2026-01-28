'''
Author : Shrinivas Umakant Jagave
Question : Find index of an element 

'''
def main():
    L = [1, 2, 3, 4, 5, 6]
    x = 5

    if x in L:
        print(L.index(x))
    else:
        raise ValueError("Value not found")

main()

