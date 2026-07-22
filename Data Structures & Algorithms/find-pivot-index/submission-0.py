class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []

        postfixSum = []


        for i in range(len(nums)):
            if len(prefixSum) == 0:
                prefixSum.append(nums[i])
            else:
                prefixSum.append(nums[i]+prefixSum[-1])
            
            if len(postfixSum) ==0:
                postfixSum.append(nums[len(nums)-1-i])
            else:
                postfixSum.append(nums[len(nums)-1-i] + postfixSum[-1])
        print(prefixSum, postfixSum[::-1])
        postfixSum = postfixSum[::-1]

        for i in range(len(prefixSum)):
            if prefixSum[i] == postfixSum[i]:
                return i
        return -1
                
            