class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack = []
        res = [0]*len(t)

        for i in range(len(t)):
            if len(stack) == 0:
                stack.append(i)
            else:
            
                while t[i] > t[stack[-1]]:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                    if len(stack)== 0:
                        break
                stack.append(i)

        return res





       




        