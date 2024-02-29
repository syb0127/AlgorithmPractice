# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root: #make sure to check the base case first
            return levels
        
        def traverseLevel(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val) #list of list니까 이 방법으로 tracking!
            if node.left: 
                traverseLevel(node.left, level+1);
            if node.right: 
                traverseLevel(node.right, level+1);

        traverseLevel(root, 0)
        return levels
            