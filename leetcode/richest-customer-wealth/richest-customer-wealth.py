# solved
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(l) for l in accounts])
