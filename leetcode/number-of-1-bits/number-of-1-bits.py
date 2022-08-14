# solved
class Solution:
    def hammingWeight(self, n: int) -> int:
        s: str = bin(n)[2:]
        return sum([int(b) for b in s])