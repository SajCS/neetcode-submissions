class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        combs = defaultdict(tuple)

        for i in nums:
            tempCombs = list(combinations(nums, i))
            for j in tempCombs:
                if len(j) == k:
                    combs[j] = list(j)
        return list(combs.values())