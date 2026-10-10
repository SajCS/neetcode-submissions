class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        intervals.sort()


        def overlap(window1, window2):
            start1, end1 = window1
            start2, end2 = window2
            return start1 <= end2 and start2<= end1

        i = 0
        while i < len(intervals) - 1:
            win1, win2 = intervals[i], intervals[i+1]
            if overlap(win1, win2):
                merge = [min(win1[0], win2[0]), max(win1[1], win2[1])]
                intervals[i] = merge
                intervals.pop(i+1)
            else:

                i += 1
        return intervals
