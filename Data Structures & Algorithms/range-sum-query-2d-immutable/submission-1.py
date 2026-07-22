class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pmat = []

        for i in matrix:
            temp = []
            for j in i:
                if len(temp) ==0:
                    temp.append(j)
                else:
                    temp.append(j + temp[-1])

            self.pmat.append(temp)
        

        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        #r1 is l and c2 r
        #anything between c1 and r2 we sum it
        res = 0
        for i in range(len(self.pmat)):
            if i >= r1 and i <= r2:
                if c1 == 0:
                    res+= self.pmat[i][c2]
                else:
                    res += self.pmat[i][c2]-self.pmat[i][c1-1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)