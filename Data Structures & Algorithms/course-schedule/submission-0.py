class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        q = deque()
        graph, inEdges = dict(), dict()
        
        for i in range(numCourses):
            graph[i] = []
            inEdges[i] = 0

        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            inEdges[pre[1]] += 1

        for i in range(numCourses):
            if inEdges[i] == 0:
                q.append(i)

        while len(q) > 0:
            element = q.popleft()
            for neighbor in graph[element]:
                inEdges[neighbor] -= 1
                if inEdges[neighbor] == 0:
                    q.append(neighbor)

        for i in range(numCourses):
            if inEdges[i] > 0:
                return False
            
        return True
        