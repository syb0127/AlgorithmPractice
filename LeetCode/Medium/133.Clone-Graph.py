"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#참고 링크: https://www.youtube.com/watch?v=mQeF6bN8hMk
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hashmap = {}
        
        #dfs이기 때문에 helper function을 쓰는게 좋음
        def dfs(node):
            if node in hashmap:
                return hashmap[node]
            #process of making the clone(copy). Node 만들어서 value만 pass in.
            cpy = Node(node.val)
            hashmap[node] = cpy
            for neighbor in node.neighbors:
                #이게 좀 헷갈릴수도 있는데 recursive 안에서도 계속 neighbor를 발견하면 neighbors 리스트를 수정 해줘야함
                cpy.neighbors.append(dfs(neighbor))
            return cpy
            
        return dfs(node) if node else None