from collections import OrderedDict

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        _map = {k, v for zip(range(n), heights)} # n
        _map = OrderedDict(sorted(_map.items(), key=lambda item: item[1])) # nlog(n)
        
        _proc_map = OrderedDict()
        for i, (num, height) in range(n): 
            _proc_map = 
        
        counts = []
        for i in range(n): 
            
