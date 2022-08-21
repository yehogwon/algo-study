# solved
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, depth: int) -> int: # return the max-length among the lengths in the tree whose root is `node`
            if node is None: 
                return depth
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        def solve(root: TreeNode) -> int: # check all the subtrees
            if root is None: 
                return 0
            cur_r = dfs(root.left, 0) + dfs(root.right, 0)
            _children = [solve(root.left), solve(root.right)]
            return max([cur_r] + _children)
        return solve(root)
