# working on it
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        _map = defaultdict(lambda: 0)
        _data = [0, 0] # sum, len
        def traversal(node): 
            _map[node.val] += 1
            _data[0] += node.val
            _data[1] += 1
            if node.left is not None: 
                traversal(node.left)
            elif node.right is not None: 
                traversal(node.right)
        traversal(root)
        
        _sum, _len = _data
        _avg = int(_sum / _len)
        print(_avg, _sum, _len, list(_map))
        return _map[_avg]
