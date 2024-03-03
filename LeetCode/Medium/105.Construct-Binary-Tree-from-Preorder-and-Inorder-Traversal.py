# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder = root, left, right
        #inorder = left, root, right
        #  3
        #9  20,15,7

        def recursion(cur_pre, cur_in):
            if not cur_pre or not cur_in:
                return
            node = TreeNode(cur_pre[0])
            root_ind = cur_in.index(cur_pre[0])
            #make sure to not include the current node
            node.left = recursion(cur_pre[1:root_ind+1], cur_in[:root_ind])
            node.right = recursion(cur_pre[root_ind+1:], cur_in[root_ind+1:])
            return node

        return recursion(preorder, inorder)
