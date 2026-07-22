class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, column = len(grid), len(grid[0])
        from collections import deque
        q = deque()

        count = 0
        i = 0
        while i < row:
            j = 0
            while j < column:
                if grid[i][j] == '1':
                    count += 1
                    q.append((i,j))
                    grid[i][j] = '0'

                while len(q) > 0:
                    element = q.popleft()
                    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
                    for d in dir:
                        x = element[0] + d[0]
                        y = element[1] + d[1]
                        if x >= 0 and x < row and y >= 0 and y < column:
                            if grid[x][y] == '1':
                                q.append((x, y))
                                grid[x][y] = '0'
                j += 1
            i += 1

        return count
        