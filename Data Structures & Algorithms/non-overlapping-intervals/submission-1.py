class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def overlap(win1, win2):
            start1, end1 = win1
            start2, end2 = win2
            return start1 < end2 and start2 < end1
        
        
        intervals.sort()
        counter = 0
        i = 0

        while i < len(intervals) -1:
            win1, win2 = intervals[i], intervals[i+1]
            if overlap(win1, win2):
                counter += 1
                if win1[1] < win2[1]:
                    intervals.pop(i+1)
                else:
                    intervals[i] = win2
                    intervals.pop(i+1)
                
            else:
                i +=1
        return counter
