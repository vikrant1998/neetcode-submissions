class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1

        i = 1
        while i < m:
            j = 1
            while j < n:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                j += 1
            i += 1

        print(dp)
        return dp[m-1][n-1]
        