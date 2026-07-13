class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        resSet = set()

        for idx, n in enumerate(nums):
            val1 = n
            i = idx + 1
            j = len(nums) - 1
            target = 0 - val1
            while i < j:
                twoSum = nums[i] + nums[j]
                if twoSum < target:
                    i += 1
                elif twoSum > target:
                    j -= 1
                else:
                    if (val1, nums[i], nums[j]) not in resSet:
                        if (val1, nums[j], nums[i]) not in resSet:
                            if (nums[i], val1, nums[j]) not in resSet:
                                if (nums[i], nums[j], val1) not in resSet:
                                    if (nums[j], val1, nums[i]) not in resSet:
                                        if (nums[j], nums[i], val1) not in resSet:
                                            resSet.add((val1, nums[i], nums[j]))
                    i += 1
                    j -= 1

        return list(resSet)

        