# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        
        def recursiveInorder(node):
            if node.left:
                recursiveInorder(node.left)
            lst.append(node.val)
            if node.right:
                recursiveInorder(node.right)
        
        recursiveInorder(root)
        return lst[k-1]