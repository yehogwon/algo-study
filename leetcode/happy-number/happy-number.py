# solved
class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_squared_digits(c: int) -> int: 
            return sum([int(s) ** 2 for s in str(c)])
        memoization = set()
        while n not in memoization: 
            if n == 1: 
                return True
            memoization.add(n)
            n = sum_squared_digits(n)
        return False
