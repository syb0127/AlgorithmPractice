# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(path_sofar, sum_sofar, node):
            if not node:
                return
            sum_sofar += node.val
            if not node.left and not node.right:
                print("inside the if")
                print(sum_sofar, targetSum)
                if sum_sofar == targetSum:
                    path_sofar.append(node.val)
                    res.append(path_sofar)
                return 
            if node.left:
                dummy = path_sofar[::]
                dummy.append(node.val)
                dfs(dummy,sum_sofar, node.left)
            if node.right:
                print("if node.right")
                dummy = path_sofar[::]
                dummy.append(node.val)
                dfs(dummy,sum_sofar, node.right)
            return

        dfs([], 0, root)
        return res