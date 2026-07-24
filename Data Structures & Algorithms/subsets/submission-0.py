class Solution:
    def __init__(self):
        self.res = []

    def recurse(self, arr, buildUp, i):
        import copy
        if i >= len(arr):
            self.res.append(copy.deepcopy(buildUp))
            return
        buildUp.append(arr[i])
        self.recurse(arr, buildUp, i + 1)
        buildUp.pop()
        self.recurse(arr, buildUp, i + 1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.recurse(nums, [], 0)
        return self.res