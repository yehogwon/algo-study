# solved
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(cur: List[int], left: List[int]) -> List[List[int]]: 
            ret = []
            if sum(cur) > target: 
                return []
            if sum(cur) == target: 
                ret += [cur]
            for i, n in enumerate(left): 
                ret += comb(cur + [n], left[i:])
            return ret
        return comb([], candidates)
