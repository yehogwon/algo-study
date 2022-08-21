# solved
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        _queue = deque([(0, root)])
        _map = defaultdict(lambda: [])
        _none = -1000
        while len(_queue) > 0: 
            _depth, _node = _queue.pop()
            if _node is None: 
                _map[_depth].append(_none)
                continue
            else: 
                _map[_depth].append(_node.val)
            _queue.appendleft((_depth + 1, _node.left))
            _queue.appendleft((_depth + 1, _node.right))
        for k, d in _map.items(): # O(n)
            if k == 0: 
                continue
            if len(d) % 2 != 0: 
                return False
            if d[:len(d) // 2] != d[-1:len(d) // 2 - 1:-1]: # it's guaranteed that length is an even number
                return False
        return True
