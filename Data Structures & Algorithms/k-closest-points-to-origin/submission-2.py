import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distancePoints = []
        res = []

        for coord in points:
            x, y = coord
            print(x,y)
        
            distance = math.sqrt(math.pow(x, 2) +math.pow(y, 2))
            distancePoints.append((distance, coord))

        print(distancePoints)
        heapq.heapify(distancePoints)
        for i in range(k):
            res.append(heapq.heappop(distancePoints)[1])

        return res

        