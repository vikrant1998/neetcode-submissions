class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffixArr = [1] * len(nums)
        prefixArr = [1] * len(nums)

        prefixArr[0] = nums[0]
        suffixArr[-1] = nums[-1]
        i = 1
        while i < len(nums):
            prefixArr[i] = nums[i] * prefixArr[i - 1] 
            i += 1

        i = len(nums) - 2
        while i >= 0:
            suffixArr[i] = nums[i] * suffixArr[i + 1]
            i -= 1

        print(nums)
        print(prefixArr)
        print(suffixArr)

        outArr = [1] * len(nums)
        i = 0
        while i < len(nums):
            if i - 1 >= 0:
                outArr[i] *= prefixArr[i - 1]
            if i + 1 < len(nums):
                outArr[i] *= suffixArr[i + 1]
            i += 1

        return outArr
        