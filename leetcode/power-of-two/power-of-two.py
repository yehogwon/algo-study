class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # check whether n is can be represented by a form of 2^x (2 to the xth power where x is an integer)
        if n == 0: 
            return False
        while True: 
            if n == 0 or n == 1: 
                return True
            if n % 2 != 0: 
                return False
            n /= 2
        