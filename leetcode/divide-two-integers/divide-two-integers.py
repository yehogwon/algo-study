# working on it
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Assume that both arguments are positive integers
        _dividend = abs(dividend)
        _divisor = abs(divisor)
        
        ret = -1
        while _dividend >= 0: 
            _dividend -= _divisor
            ret += 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0): ret = -ret
        return ret