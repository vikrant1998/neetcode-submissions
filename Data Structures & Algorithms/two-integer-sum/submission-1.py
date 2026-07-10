class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoMap = dict()
        for idx, n in enumerate(nums):
            twoMap[n] = idx

        for idx, n in enumerate(nums):
            num1 = n
            num2 = target - n
            if num2 in twoMap and twoMap[num2] != idx:
                return [idx, twoMap[num2]]