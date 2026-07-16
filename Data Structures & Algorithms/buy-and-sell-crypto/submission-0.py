class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        maxDiff = 0
        minVal = float('inf')
        while i < len(prices):
            minVal = min(prices[i-1], minVal)
            maxDiff = max(maxDiff, prices[i] - minVal)
            i += 1

        return maxDiff

        