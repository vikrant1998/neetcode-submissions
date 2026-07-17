class Solution:
    def __init__(self):
        self.cache = dict()

    def recurse(self, n):
        if n == 1: return 1
        if n == 2: return 2
        if n in self.cache: return self.cache[n]
        res1 = self.cache[n - 1] if n - 1 in self.cache else self.recurse(n - 1)
        if n - 1 not in self.cache: self.cache[n - 1] = res1
        res2 = self.cache[n - 2] if n - 2 in self.cache else self.recurse(n - 2)
        if n - 2 not in self.cache: self.cache[n - 2] = res2
        return res1 + res2

    def climbStairs(self, n: int) -> int:
        return self.recurse(n)
        