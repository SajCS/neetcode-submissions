class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []

        

        def helper(i, curComb):
            if len(curComb) == k:
                combs.append(curComb.copy())
                return

            if i > n:
                return

            curComb.append(i)
            helper(i+1, curComb)
            curComb.pop()


            helper(i+1, curComb)


        helper(1,[])
        return combs