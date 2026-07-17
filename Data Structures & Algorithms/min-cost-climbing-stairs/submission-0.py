class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = (len(cost) + 1) * [0]
        dp[0] = cost[0]
        dp[1] = cost[1]
        if len(cost) == 2: return min(dp[0], dp[1])

        i = 2
        while i < len(cost):
            dp[i] += min(dp[i - 1], dp[i - 2]) + cost[i]
            i += 1

        return min(dp[len(cost) - 1], dp[len(cost) - 2])
        