class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []


        def dfs(i, curset, total):
            if total == target:
                combs.append(curset.copy())
                return
            if i >= len(nums) or total > target:
                return

            
            curset.append(nums[i])
            dfs(i, curset, total + nums[i])
            curset.pop()


            dfs(i+1, curset, total)
        dfs(0, [], 0)
        return combs
