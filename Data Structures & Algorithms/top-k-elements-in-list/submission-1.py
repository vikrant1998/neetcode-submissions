class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        numDict = dict()

        for n in nums:
            if n in numDict: numDict[n] += 1
            else: numDict[n] = 1

        for key, v in numDict.items(): freq[v].append(key)

        res = []
        i = len(nums)

        while i > 0:
            for element in freq[i]:
                res.append(element)
                if len(res) == k:
                    return res
            i -= 1

        return res