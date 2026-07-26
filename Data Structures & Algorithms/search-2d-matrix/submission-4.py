class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        top, bot = 0, len(matrix)-1
    
        while top <= bot:
            midrow = (top + bot)//2
            if target > matrix[midrow][-1]:
                top = midrow +1
            elif target < matrix[midrow][0]:
                bot = midrow - 1
            else:

                l, r = 0, len(matrix[midrow])-1
                while l <= r:
                    mid = (l+r)//2
                    if matrix[midrow][mid] < target:
                        l = mid +1
                    elif matrix[midrow][mid] > target:
                        r = mid -1
                    else:
                        return True
                return False
        return False






        

        