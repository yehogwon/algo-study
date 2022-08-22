# solved
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: 
            return False
        _bin = [int(a) for a in "{0:b}".format(n)][::-1]
        _ones = []
        for i, b in enumerate(_bin): 
            if b == 1: 
                _ones.append(i)
        if len(_ones) == 1 and _ones[0] % 2 == 0: 
            return True
        else: 
            return False
