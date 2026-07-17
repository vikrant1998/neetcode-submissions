class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for n in nums:
            if n not in numSet:
                numSet.add(n)
            else:
                return n