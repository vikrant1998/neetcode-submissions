class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            return -1

        from bisect import bisect_right
        idx = bisect_right(nums, target)
        if nums[idx-1] == target: return idx-1
        return -1
        