class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n+1) for _ in range(m+1)]

        i = 1
        while i <= m:
            j = 1
            while j <= n:
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                j += 1
            i += 1

        return dp[m][n]

        