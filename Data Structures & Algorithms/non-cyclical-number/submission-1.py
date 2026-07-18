class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        prevSums = set()
        doubleCheck = True
        while res != 1 and doubleCheck:
            outRes = list(str(res))
            sumRes = 0
            for o in outRes: sumRes += int(o) ** 2
            if sumRes in prevSums:
                return False
            prevSums.add(sumRes)
            res = sumRes
        if res == 1:
            return True
        return False
