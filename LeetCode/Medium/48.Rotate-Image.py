class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0])-1
        
        while right > left:
            for i in range(right-left):
                top, bottom = left, right
                #temporary variable for storing the 
                topleft = matrix[top][i+left]
                print
                #move bottom left to top left 
                matrix[top][i+left] = matrix[bottom-i][left]
                #move bottom right to bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                #move top right to bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                #move top left to top right
                matrix[top+i][right] = topleft
            right -= 1
            left += 1