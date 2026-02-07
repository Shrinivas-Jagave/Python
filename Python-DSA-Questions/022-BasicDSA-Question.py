'''
Author : Shrinivas Umakant Jagave
Question : (a + b)**2 = a**2 + 2ab + b**2.

'''
def Expression(a:float, b:float)->float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Bad Type")
    
    return a**2 + 2*a*b + b**2


print(Expression(2, 3))
