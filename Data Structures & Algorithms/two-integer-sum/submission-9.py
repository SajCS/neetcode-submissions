class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hmap:
                print(val, i , hmap)
                return [hmap[val], i]
            else:
                hmap[nums[i]] = i
