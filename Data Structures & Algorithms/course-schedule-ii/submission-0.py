class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        q = deque()
        graph, inEdges = dict(), dict()
        finList = []

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
            finList.append(element)
            for neighbor in graph[element]:
                inEdges[neighbor] -= 1
                if inEdges[neighbor] == 0:
                    q.append(neighbor)

        for i in range(numCourses):
            if inEdges[i] > 0:
                return []
            
        return finList[::-1]
        