# solved
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # find the two bars between which the maximum area is formed
        # second, use two-pointer technique
        def area(i, j): # area form by the two lines; height[i] and height[j]
            # suppose that j >= i; i and j is in order. 
            return (j - i) * min(height[i], height[j])
        _max = 0
        i, j = 0, len(height) - 1
        while i < j: 
            _max = max(_max, area(i, j))
            if height[i] <= height[j]: # try to find the higher bar
                i += 1
            else: 
                j -= 1
        return _max
