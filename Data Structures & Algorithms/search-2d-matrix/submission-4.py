from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 1. Define low and high pointers for the entire matrix as a flat list
        low = 0
        high = (rows * cols) - 1
        
        # 2. Run a single binary search loop
        while low <= high:
            mid = (low + high) // 2
            
            # 3. Use math to map the 1D 'mid' index directly to 2D matrix coordinates
            r = mid // cols
            c = mid % cols
            
            # 4. Compare and adjust pointers
            if matrix[r][c] == target:
                return True
            elif target < matrix[r][c]:
                high = mid - 1
            else:
                low = mid + 1
                
        return False
