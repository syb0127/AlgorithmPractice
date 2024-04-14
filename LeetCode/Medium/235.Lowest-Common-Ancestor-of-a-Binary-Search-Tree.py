# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #recursive approach => adjust root depending on whether p.val is <, >, or == to p or q
        if (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else: #accounts for all cases where root is either p OR q OR is a splitting point(LCA node) between p and q
            return root