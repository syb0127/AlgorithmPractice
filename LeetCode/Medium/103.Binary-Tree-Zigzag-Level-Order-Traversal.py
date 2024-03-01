# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)

        #iterative bfs
        while queue:
            #queue는 늘었다 줄었다 할것임
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                cur_node = queue.popleft()
                if not cur_node:
                    continue
                level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(level)

        for i in range(1,len(result),2):
            result[i].reverse()

        return result