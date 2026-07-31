class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        left = 0
        visitedMap = dict()
        maxLen = 0
        while right < len(s):
            if s[right] in visitedMap and visitedMap[s[right]] >= left:
                left = visitedMap[s[right]] + 1
            visitedMap[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
            right += 1
            
        return maxLen
        