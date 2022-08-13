class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rev = digits[::-1]
        rev[0] += 1
        for i in range(len(rev) - 1): 
            if rev[i] == 10: 
                rev[i] = 0
                rev[i + 1] += 1
        if rev[-1] == 10: 
            rev[-1] = 0
            rev += [1]
        return rev[::-1]
        