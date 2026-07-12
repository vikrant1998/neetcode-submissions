class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.inpArr = []
        self.k = k
        for n in nums:
            heapq.heappush(self.inpArr, n)

    def add(self, val: int) -> int:
        import heapq
        heapq.heappush(self.inpArr, val)

        v = len(self.inpArr) - self.k   # discard this many smallest
        vals = []
        while v > 0:
            vals.append(heapq.heappop(self.inpArr))
            v -= 1
        res = self.inpArr[0]            # k-th largest = root of what remains
        for x in vals:
            heapq.heappush(self.inpArr, x)
        return res