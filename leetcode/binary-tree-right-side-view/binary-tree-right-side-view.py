# solved
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []
        
        traversal = [root.val] # traversal[depth] = the most-right value
        _queue = deque([(0, root)])
        # DFS
        while len(_queue) > 0: 
            _depth, _node = _queue.pop()
            try: 
                traversal[_depth] = _node.val
            except: 
                traversal.append(_node.val)
            if _node.left is not None: 
                _queue.appendleft((_depth + 1, _node.left))
            if _node.right is not None: 
                _queue.appendleft((_depth + 1, _node.right))
            
        return traversal
