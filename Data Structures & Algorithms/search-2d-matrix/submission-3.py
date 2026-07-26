class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        contain = None
        for i in range(len(matrix)):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                print("ye")
                contain = matrix[i]
        if contain == None:
            return False
        l, r = 0, len(contain) -1

        while l <= r:
            mid = (l+r)//2
            if contain[mid] < target:
                l = mid +1
            elif contain[mid] > target:
                r = mid -1
            else:
                return True
        return False
        

        