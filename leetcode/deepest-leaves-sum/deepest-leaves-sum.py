# solved
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        traversal = [] # traversal[depth] = sum of the values of nodes in ith depth
        _queue = deque([(0, root)])
        # DFS
        while len(_queue) > 0: 
            _depth, _node = _queue.pop()
            try: 
                traversal[_depth] += _node.val
            except: 
                traversal.append(_node.val)
            if _node.left is not None: 
                _queue.appendleft((_depth + 1, _node.left))
            if _node.right is not None: 
                _queue.appendleft((_depth + 1, _node.right))
        return traversal[-1]
        