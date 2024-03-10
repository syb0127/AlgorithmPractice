# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, sum):
            #print(node.val, sum)
            nonlocal total
            if (not node.left and not node.right):
                # print(int(sum+str(node.val)))
                total += int(sum+str(node.val))
                return
            if (node.left):
                # print(node)
                # print(sum+str(root.val))
                dfs(node.left, sum+str(node.val))
            if (node.right):
                #print(node.left)
                #print(sum+str(root.val))
                dfs(node.right, sum+str(node.val))
            return
        dfs(root,"")
        return total