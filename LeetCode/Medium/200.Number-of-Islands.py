class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #you don't need a "seen" set since you are changing the values as you are iterating
        num_islands = 0

        def dfs(row, col):
            if (row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == '0'):
                return
            grid[row][col]  = '0'
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(i, j)

        return num_islands