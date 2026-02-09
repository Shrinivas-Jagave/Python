'''
Author : Shrinivas Umakant Jagave
Question : Convert decimal to binary 
'''

def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    
    return binary

print(decimal_to_binary(13))
