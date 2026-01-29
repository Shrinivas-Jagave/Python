'''
Author : Shrinivas Umakant Jagave
Question : Count digits in a number
'''

def CountOfDigit(num:int)->int:
    if not isinstance(num, int):
        raise TypeError("Type error")
    if num == 0:
        return 1
    if num < 0:
        num = abs(num)

    i = 0
    while (num != 0):
        num = num // 10
        i += 1

    return i
    

def main():
    num = -596545555

    print(CountOfDigit(num))

main()
