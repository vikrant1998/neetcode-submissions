class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        from collections import deque
        q = deque()
        maxArea = 0

        i = 0
        while i < m:
            j = 0
            while j < n:

                area = 0
                if grid[i][j] == 1:
                    q.append([i, j])
                    grid[i][j] = 0
                    area = 1

                axis = [[-1,0], [0,1], [1,0], [0,-1]]
                while len(q) > 0:
                    element = q.popleft()
                    for coord in axis:
                        x, y = coord
                        x += element[0]
                        y += element[1]
                        if x >= 0 and x < m and y >= 0 and y < n:
                            if grid[x][y] == 1:
                                q.append([x, y])
                                grid[x][y] = 0
                                area += 1

                maxArea = max(maxArea, area)

                j += 1
            i += 1

        return maxArea
        