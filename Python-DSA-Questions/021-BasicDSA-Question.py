'''
Author : Shrinivas Umakant Jagave
Question : Sum of digits of a number.

'''

def SumOfDigitOfNumber(Num:int)->int:
    if not isinstance(Num, int):
        raise TypeError("Bad Type")
    
    if Num == 0:
        return 0

    return sum(int(x) for x in str(abs(Num)))


print(SumOfDigitOfNumber(-123))