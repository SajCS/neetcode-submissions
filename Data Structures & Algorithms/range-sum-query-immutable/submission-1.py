class NumArray:

    def __init__(self, nums: List[int]):
        self.pnums = []
        for i in nums:
            if len(self.pnums) <= 0:
                self.pnums.append(i)
            else:
                self.pnums.append(self.pnums[-1]+i)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pnums[right]
        else:
            return self.pnums[right]-self.pnums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)