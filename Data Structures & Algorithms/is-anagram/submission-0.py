class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMapS, charMapT = dict(), dict()

        for sc in s:
            if sc in charMapS: charMapS[sc] += 1
            else: charMapS[sc] = 0

        for st in t:
            if st in charMapT: charMapT[st] += 1
            else: charMapT[st] = 0

        if len(charMapS) != len(charMapT): return False

        for key, value in charMapS.items():
            if key not in charMapT:
                return False
            if value != charMapT[key]:
                return False
        return True        