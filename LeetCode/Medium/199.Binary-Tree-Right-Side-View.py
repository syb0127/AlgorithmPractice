# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final_lst = []
        
        def rightmostNodes(depth, node):
            if not node:
                return
            if len(final_lst)-1 < depth:
                final_lst.append(node.val)
            rightmostNodes(depth+1, node.right)
            rightmostNodes(depth+1, node.left)
            return
        rightmostNodes(0, root)

        return final_lst