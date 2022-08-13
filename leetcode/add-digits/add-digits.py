class Solution:
    def addDigits(self, num: int) -> int:
        def solve(n: int): 
            if n // 10 == 0: 
                return n;
            _sum = sum([int(s) for s in str(n)])
            return solve(_sum)
        return solve(num)