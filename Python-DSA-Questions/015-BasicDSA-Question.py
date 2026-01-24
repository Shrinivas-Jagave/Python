'''
Author : Shrinivas Umakant Jagave
Question : Find the length of a string without len() 

'''

def lenOf(string:str)->int:
    if not isinstance(string, str):
        raise TypeError("Type Error")
    
    length = 0

    for x in string:
        length += 1

    return length

def main():
    string = "Shrinivas Umakant Jagave"
    print(lenOf(string))

main()
