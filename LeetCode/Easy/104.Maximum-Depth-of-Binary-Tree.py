# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def recurse(tree):
            if not tree:
                return 0
            left_height = recurse(tree.left)
            right_height = recurse(tree.right)
            return max(left_height, right_height)+1
        
        return recurse(root)