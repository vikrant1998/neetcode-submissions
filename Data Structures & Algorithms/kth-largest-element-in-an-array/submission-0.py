class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        q = []
        for n in nums:
            if len(q) < k:
                heapq.heappush(q, n)
            else:
                heapq.heappush(q, n)
                heapq.heappop(q)

        return q[0]
        