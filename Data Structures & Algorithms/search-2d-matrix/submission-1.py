class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        from bisect import bisect_right
        i = 0
        mArr = []
        while i < len(matrix):
            mArr.append(matrix[i][0])
            i += 1

        idx = bisect_right(mArr, target)
        idx -= 1

        if idx < 0: return False
        i = 0
        fArr = []
        while i < len(matrix[0]):
            fArr.append(matrix[idx][i])
            i += 1

        idx1 = bisect_right(fArr, target)
        idx1 -= 1
        if idx1 >= 0 and idx1 < len(fArr) and fArr[idx1] == target:
            return True

        return False