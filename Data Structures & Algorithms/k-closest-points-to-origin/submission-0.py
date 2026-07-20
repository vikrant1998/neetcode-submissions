class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math
        q = []
        for coord in points:
            dist = math.sqrt((coord[0])**2 + (coord[1])**2)
            heapq.heappush(q, (dist, coord))

        res = []
        while k != 0:
            dist, coord = heapq.heappop(q)
            res.append(coord)
            k -= 1
        return res