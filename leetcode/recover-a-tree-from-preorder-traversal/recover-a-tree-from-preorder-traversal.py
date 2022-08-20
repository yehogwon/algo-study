# solved
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # preprocessing
        _proc = [] # list of tuples: (depth, value)
        _depth = 0

        i = 0
        while i < len(traversal): # O(n)
            c = traversal[i]
            if c == '-': 
                _depth += 1
                i += 1
            else: 
                jdx = i
                while jdx < len(traversal) and traversal[jdx] != '-': 
                    jdx += 1
                _proc.append((_depth, int(traversal[i:jdx])))
                _depth = 0
                i = jdx

        root = TreeNode(_proc[0][1])
        _stack = [(_proc[0], root)]

        def _insert(parent: TreeNode, child: TreeNode): 
            if parent.left is None: 
                parent.left = child
            elif parent.right is None: 
                parent.right = child
            else: 
                raise ValueError("Parent's children sits are already being occupied. ")

        i = 1
        depth = 1
        while i < len(_proc): # O(n)
            if _proc[i][0] == _stack[-1][0][0] + 1: 
                node = TreeNode(_proc[i][1])
                _insert(_stack[-1][1], node)
                _stack.append((_proc[i], node))
                i += 1
            else: 
                _stack.pop()
        return root
