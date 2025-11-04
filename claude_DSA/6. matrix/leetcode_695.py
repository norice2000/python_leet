# You are given an m x n binary matrix grid. An island is a group of 1's 
# (representing land) connected 4-directionally (horizontal or vertical). 
# You may assume all four edges of the grid are surrounded by water.

# The AREA of an island is the number of cells with a value 1 in the island.

# Return the MAXIMUM area of an island in grid. If there is no island, return 0.

# Example 1:
# Input: grid = [
#   [0,0,1,0,0,0,0,1,0,0,0,0,0],
#   [0,0,0,0,0,0,0,1,1,1,0,0,0],
#   [0,1,1,0,1,0,0,0,0,0,0,0,0],
#   [0,1,0,0,1,1,0,0,1,0,1,0,0],
#   [0,1,0,0,1,1,0,0,1,1,1,0,0],
#   [0,0,0,0,0,0,0,0,0,0,1,0,0],
#   [0,0,0,0,0,0,0,1,1,1,0,0,0],
#   [0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]
# Output: 6

# Explanation: The answer is 6, not 11. The island with area 6 is shown:
#   [0,0,0,0,0,0]
#   [0,0,0,0,0,0]
#   [0,0,0,0,0,0]
#   [0,0,0,0,1,0]
#   [0,0,0,0,1,1]  ← This island
#   [0,0,0,0,0,1]
#   [0,0,0,0,0,0]
# ```

# ### **Simpler Example:**
# ```
# Input: grid = [
#   [1,1,0],
#   [1,0,0],
#   [0,0,1]
# ]
# Output: 3

# Explanation:
# Island 1: 3 cells (top-left cluster)
# Island 2: 1 cell (bottom-right)
# Maximum = 3

class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        
        def dfs(r, c):
            # Base cases - what should you return?
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return
            # Mark visited
            grid[r][c] = 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            
            # Count this cell + all neighbors
            # How do you add them up?
            
        # Loop through grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Get area of this island
                    # Update max_area

                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)
                    pass
        
        return max_area
    
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
sol = Solution()
print(sol.maxAreaOfIsland(grid))