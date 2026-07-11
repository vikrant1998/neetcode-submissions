class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i = 0
        runSum, maxSum = float('-inf'), float('-inf')
        while i < len(nums):
            runSum = max(nums[i], nums[i] + runSum)
            maxSum = max(maxSum, runSum)
            i += 1
        return maxSum
        