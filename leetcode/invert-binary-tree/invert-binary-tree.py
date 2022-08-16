# solved
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap(node): 
            _tmp = node.left
            node.left = node.right
            node.right = _tmp
        def reverse(node): 
            if node is None: 
                return
            if node.left is None and node.right is None: 
                return
            if node.left is not None: 
                reverse(node.left)
            if node.right is not None: 
                reverse(node.right)
            swap(node)
        reverse(root)
        return root
                