# solved
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = tuple(nums)
        subset_set = set()
        def gen_subsets(items): 
            subset_set.add(items)
            for i in range(len(items)): 
                gen_subsets(items[:i] + items[i+1:])
        gen_subsets(nums)
        return list(subset_set)
