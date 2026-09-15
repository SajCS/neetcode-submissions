import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            res = abs(stone1 - stone2)
            if res != 0:
                heapq.heappush_max(stones,res)
        if len(stones) == 0:
            return 0
        return stones[0]
        
