class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False

        hmap ={
            ")":"(",
            "}":"{",
            "]":"["

        }


        stack = []

        for i in s:
            if i not in hmap:
                stack.append(i)
            else:
                if len(stack) ==0:
                    return False
                if stack[-1] == hmap[i]:
                    print("hello")
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


        



    




    
     



    
       

