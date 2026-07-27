[1, 1, 3, 3]

[]



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp = [0] * (len(nums))
        dp[0] = nums[0]
        i = 1
        while i < len(nums):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            i += 1

        return dp[-1]
        