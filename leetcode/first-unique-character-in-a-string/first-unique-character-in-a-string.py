from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        lookup = defaultdict(lambda: 0)
        for c in s: 
            lookup[c] += 1
        for i, c in enumerate(s): 
            if lookup[c] == 1: # average O(1)
                return i
        return -1
