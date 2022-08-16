# solved
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i, j = 0, 0 # i for non-zeroes, j for zeroes
        while i < len(nums) and j < len(nums): 
            if nums[i] == 0: 
                i += 1
                continue
            if nums[j] != 0: 
                j += 1
                continue
            if i > j: 
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
