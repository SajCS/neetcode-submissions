class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        subsets, curSet = [], []
        def helper(i):
            if i >= len(nums):
                subsets.append(curSet.copy())
                return

            #To include

            curSet.append(nums[i])
            helper(i+1)
            curSet.pop()

            # to not include

            while i + 1 < len(nums) and nums[i] == nums[i+ 1]:
                i += 1
            helper(i + 1)

        helper(0)

  
        return subsets
    
            
