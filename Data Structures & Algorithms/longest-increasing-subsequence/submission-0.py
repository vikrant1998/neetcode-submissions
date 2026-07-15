class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        from bisect import bisect_left
        arrList = []
        i = 0
        while i < len(nums):
            idx = bisect_left(arrList, nums[i])
            if idx == len(arrList):
                arrList.append(nums[i])
            else:
                arrList[idx] = nums[i]
            i += 1

        return len(arrList)
        