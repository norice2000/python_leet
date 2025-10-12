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
        if not grid:
            return 0
        
        row = len(grid) 
        col = len(grid[0])
        island = 0

        # create this second
        def dfs(r, c):
            if r < 0 or r >= row: # this makes sure you dont go out of bound of the grid for rows
                return
            if c < 0 or c >= col: # this makes sure you dont go out of bound of the grid for columns
                return
            if grid[r][c] == '0': 
                return
        
            # Mark current cell as visited
            grid[r][c] = '0'
            # Explore 4 directions (no 'grid' parameter)
            dfs(r, c+1) # this will now go right
            dfs(r+1, c) # this will now go down
            dfs(r, c-1) # this will now go left
            dfs(r-1, c) # this will now go up


        # create this first!!!
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    island += 1
                    dfs(r,c)

        return island

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

sol = Solution()
print(sol.numIslands(grid))
#Output: 3