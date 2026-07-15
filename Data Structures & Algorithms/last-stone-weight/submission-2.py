class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        q = []
        for s in stones: heapq.heappush(q, -1 * s)

        while len(q) >= 2:
            element1 = heapq.heappop(q)
            element2 = heapq.heappop(q)
            if element1 == element2: continue
            else: heapq.heappush(q, (element1 - element2))

        if len(q) == 0: return 0
        if len(q) == 1: return -1 * q[0]
        