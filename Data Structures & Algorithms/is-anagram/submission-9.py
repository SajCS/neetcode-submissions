class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmaps = defaultdict(int)
        hmapt = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hmaps[s[i]] += 1
            hmapt[t[i]] += 1
        
        

        return hmaps == hmapt
        
    
            