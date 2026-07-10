class Solution:

    def encode(self, strs: List[str]) -> str:
        resStr = ''
        for s in strs: resStr += str(len(s)) + '#' + s
        return resStr

    def decode(self, s: str) -> List[str]:
        i = 0
        resStr = []
        while i < len(s):
            j = i
            numStr = ''
            while j < len(s) and s[j] != '#':
                numStr += s[j]
                j += 1

            num = int(numStr)
            j += 1
            k = j
            fStr = ''
            while k < len(s) and k < j + num:
                fStr += s[k]
                k += 1
            j = k
            resStr.append(fStr)
            i = j
        return resStr
