# solved
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def _permute(prefix: List[int], rests: List[int]) -> str: 
            if len(rests) == 0: 
                result.append(prefix)
                return prefix
            else: 
                permutations = []
                for i, n in enumerate(rests): 
                    permutations += _permute(prefix + [n], rests[:i] + rests[i + 1:])
                return permutations
        _permute([], nums)
        return result
