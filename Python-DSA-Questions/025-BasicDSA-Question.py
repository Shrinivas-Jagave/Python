'''
Author : Shrinivas Umakant Jagave
Question :  Performs operations on a list up to a given target index. Returns sum, square, and cube of the sum.
'''

from typing import Tuple

class ListOperation:
    def __init__(self, init_L: list, init_Target: int):
        if not isinstance(init_L, list) or not isinstance(init_Target, int):
            raise TypeError('bad type')
        
        if not init_L:
            raise ValueError("List should not be empty")
        
        if init_Target <= 0:
            raise ValueError("Target must be positive")
        
        if init_Target > len(init_L):
            raise ValueError("Target exceeds list length")
        
        self.L = init_L
        self.Target = init_Target

    def calculate(self) -> Tuple[int, int, int]:
        result = 0
        for E in self.L[:self.Target]:
            result += E

        return result, result**2, result**3


S = ListOperation([3, 4, 5, 6, 7, 8, 9], 2)
print(S.calculate())