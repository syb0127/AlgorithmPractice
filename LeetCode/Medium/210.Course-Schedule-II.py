from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        final_lst = []
        indegree = [0 for _ in range(numCourses)]
        adjacency_lst = [[]  for _ in range(numCourses)]
        
        for pre in prerequisites:
            indegree[pre[0]] += 1
            #map from a prerequisite to a course; Don't get confused with the indegree array since it's the other way around
            adjacency_lst[pre[1]].append(pre[0])

        q = deque()
        for i in range(len(adjacency_lst)):
            if indegree[i] == 0:
                q.append(i)
        if not q:
            return []
        while q:
            cur_course = q.popleft()
            final_lst.append(cur_course)
            for prereq in adjacency_lst[cur_course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    q.append(prereq)
        if len(final_lst) != numCourses:
            return []
        return final_lst