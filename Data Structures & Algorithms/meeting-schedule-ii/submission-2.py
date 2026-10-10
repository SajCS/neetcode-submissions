"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = []
        if not intervals:
            return 0
  
        for i in intervals:
            meetings.append((i.start, i.end))
        meetings.sort()
        # print(meetings)
        # def overlap(win1, win2):
        #     start1, end1 = win1
        #     start2, end2 = win2
        #     return start1 < end2 and start2 < end1
        heap = []
        for i in meetings:
            if len(heap) ==0:
                heapq.heappush(heap, i[1])
            else:
                if i[0] >= heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, i[1])
                else:
                    heapq.heappush(heap, i[1])
        return len(heap)

