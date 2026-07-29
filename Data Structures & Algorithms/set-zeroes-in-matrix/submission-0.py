class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = set()
        col = set()

        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
                j += 1
            i += 1

        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if i in row:
                    matrix[i][j] = 0
                if j in col:
                    matrix[i][j] = 0
                j += 1
            i += 1
        
        