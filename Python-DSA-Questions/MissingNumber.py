def MissingNumberInList(L:list)->int:
    if not isinstance(L, list):
        raise TypeError("Bad type")
    
    if not L:
        raise ValueError("List should not be empty")
    
    result = 0

    L.sort()

    for x in L:
        if type(x) != int:
            raise ValueError("Values should be integer")
        result += x
        
    n = L[len(L) - 1]
    addition = n * (n + 1) / 2
    addition = int(addition)

    if addition == result:
        return n + 1
    
    missingnumber = addition - result

    if missingnumber > n:
        print(result, n)
        raise ValueError("2 or more numbers are missing")
    
    return missingnumber
    


def main():
    L = [1, 2, 3, 4, 5, 6, 8, 9, 7]
    print(MissingNumberInList(L))

main()
