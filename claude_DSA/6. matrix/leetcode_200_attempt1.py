# Given a 2D grid of '1's (land) and '0's (water), 
# count the number of islands.

# Input:
# grid = [
#   ["1","1","0","0","0"], 
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 5 ints in rows (across)
# 4 ints in columns (downwards)
# Output: 3

#         Column 0  Column 1  Column 2
#              ↓         ↓         ↓
# Row 0 →   [  1    ,    1    ,    0   ]
# Row 1 →   [  1    ,    1    ,    0   ]
# Row 2 →   [  0    ,    0    ,    1   ]

# grid[i][j]
#      ↑  ↑
#      │  └─ j = column index (which column)
#      └──── i = row index (which row)

# An island is surrounded by water and is formed by 
# connecting adjacent lands horizontally or vertically.

class Solution:
    def numIslands(self, grid) -> int:
        # edge case of not grid: return 0

        # we want the legnth for rows and columns
        rows = len(grid)
        colums = len(grid[0])

        # def dfs(r,c)
        # check that we dont go out of bound
        # if r < 0 or r >= rows or c < 0 or c >= columns or grid == '0'
        # return
        # else
        # append it as 0 from 1 to indicate that we already seen in
        # grid[r][c] = '0'
        # dfs(r-1, c)
        # dfs(r+1, c)
        # dfs(r, c-1)
        # dfs(r, c+1)

        # island = 0
        # for r in rows
        # for c in coumns
        # if grid[r][c] == '1'
        #islands += 1
        # dfs
        # return islands
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= colums or grid[r][c] == '0':
                return
            else:
                grid[r][c] = '0'
                dfs(r-1, c)
                dfs(r+1, c)
                dfs(r, c-1)
                dfs(r, c+1)

        islands = 0
        for r in range(rows):
            for c in range (colums):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        return islands
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid))
#Output: 3