"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = collections.deque([root])
        
        while q:
            size = len(q)
            for i in range(size):
                cur_node = q.popleft()
                
                if i < size-1:
                    #next node on the queue
                    cur_node.next = q[0]
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

        return root