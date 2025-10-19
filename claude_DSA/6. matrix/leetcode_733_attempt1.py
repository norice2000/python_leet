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

class Solution:
    def floodFill(self, image, sr, sc, color):
        #edge case
        #need orginal image to compare
        # need length of rows and columns
        #dfs(r, c)
        # check it does not go out of bound

        # call dfs func
        if image[sr][sc] == color:
            return image
        
        rows = len(image)
        columns = len(image[0])
        original_image = image[sr][sc]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= columns or image[r][c] != original_image:
                return
            image[r][c] = color
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        dfs(sr, sc)
        return image
        
    
image = [[1,1,1],
         [1,1,0],
         [1,0,1]]

sol = Solution()
print(sol.floodFill(image, color=2, sr=1, sc=1))