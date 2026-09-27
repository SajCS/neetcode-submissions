class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        combs = []
        dic = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"], 
            "4": ["g", "h", "i"], 
            "5": ["j", "k", "l"], 
            "6": ["m", "n", "o"], 
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"], 
            "9": ["w", "x", "y", "z"]

        }

        def helper(i, curComb):

            if len(curComb) == len(digits):
                combs.append(curComb)
                return 
            
            

            for j in dic[digits[i]]:
                
                

                helper(i+1, curComb+j)
            
        helper(0, "")
        if combs[0] == "":
            return []
        return combs

        


                
                

            

        