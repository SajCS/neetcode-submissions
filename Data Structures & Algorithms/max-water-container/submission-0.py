class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hval = 0

        l, r = 0, len(heights)-1

        while l<r:
            if min(heights[l], heights[r])* (r-l) >hval:
                hval = min(heights[l], heights[r])* (r-l)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return hval
  
        