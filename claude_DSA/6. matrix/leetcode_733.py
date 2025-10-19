# You're given an image represented by a 2D array of integers, where each 
# integer represents the pixel value of the image. You're also given:
# - sr, sc: starting pixel row and column
# - color: new color to fill

# Perform a "flood fill" starting from pixel (sr, sc). 

# A flood fill changes the color of the starting pixel and all pixels 
# connected to it (4-directionally) that have the SAME color as the 
# starting pixel.

# Example:
# Input: 
# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]
# sr = 1, sc = 1, color = 2

# Output: 
# [[2,2,2],
#  [2,2,0],
#  [2,0,1]]

# Explanation:
# Starting at (1,1) with value 1, change all connected 1's to 2.
# ```

# ### **Visual:**
# ```
# Before:          After:
# 1 1 1            2 2 2
# 1 1 0    →       2 2 0
# 1 0 1            2 0 1

# Starting at middle (1,1), all connected 1's become 2's.
# The bottom-left 1 is NOT connected (separated by 0).

class Solution:
    def floodFill(self, image, sr, sc, color):
        if image[sr][sc] == color:
            return image
        # What do you need to track?
        rows = len(image)
        columns = len(image[0])
        # Hint: What was the original color?
        original_color = image[sr][sc]
        
        def dfs(r, c):
            # What are your base cases?
            if r < 0 or r >= rows or c < 0 or c >= columns or image[r][c] != original_color:
                return
            # When should you stop exploring?
            # else:
        # Change the color
            image[r][c] = color
        # Explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)
    
        # # Start the flood fill
        # for r in range(rows):
        #     for c in range(columns):
        #         if image[r][c] == 1:
        dfs(sr, sc)
        return image
    
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]

sol = Solution()
print(sol.floodFill(image, color=2, sr=1, sc=1))