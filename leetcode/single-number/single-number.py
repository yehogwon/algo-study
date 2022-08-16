# solved
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _unique = 0
        for n in nums: 
            _unique ^= n
        return _unique
