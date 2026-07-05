class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##We can use counter to get each elements

        bucket = [[] for i in range(len(nums)+1)]
        
        counter = Counter(nums)

        print(counter)

        for key, freq in counter.items():
            bucket[freq].append(key)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)

            if len(res) == k:
                return res


        
        
        
    
       

        

    


        

