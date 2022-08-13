class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0
        while True: 
            if n ** 2 > x: 
                break
            n += 1
        return n - 1