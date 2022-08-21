# solved
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[i] for tup in zip(range(len(nums) // 2), range(len(nums) // 2, len(nums))) for i in tup]
