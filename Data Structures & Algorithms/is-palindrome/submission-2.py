class Solution:
    def isPalindrome(self, s: str) -> bool:
        inpStr = ''
        for c in s:
            if not c.isalnum(): continue
            inpStr += c.lower()

        i, j = 0, len(inpStr) - 1
        while i < j:
            if inpStr[i] != inpStr[j]:
                return False
            i += 1
            j -= 1
        return True
        