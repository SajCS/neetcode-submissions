class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        i = 0

        def overlap(win1, win2):
            start1, end1 = win1
            start2, end2 = win2
            return start1 <= end2 and start2 <= end1

        while i < len(intervals)-1:
            win1 , win2 = intervals[i], intervals[i+1]
            if overlap(win1, win2):
                merge = [min(win1[0], win2[0]), max(win1[1],win2[1])]
                intervals[i] = merge
                intervals.pop(i+1)
            else:
                i+= 1
        return intervals
            
            
