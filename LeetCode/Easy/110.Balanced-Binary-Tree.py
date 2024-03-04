# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #build a helper function that calculates the height for us
    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif (abs(self.height(root.left)-self.height(root.right)) < 2):
            if (self.isBalanced(root.right) and self.isBalanced(root.left)):
                return True
        return False