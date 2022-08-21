# solved
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(lambda: 0)
        for n in nums: 
            d[n] += 1
        return max(d, key=d.get)
