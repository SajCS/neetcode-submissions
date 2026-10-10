"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = []
        if intervals:
            for i in intervals:
                meetings.append((i.start, i.end))
        meetings.sort()
        print(meetings)

        def overlap(win1, win2):
            start1, end1 = win1
            start2, end2 = win2
            return start1< end2 and start2 < end1

        
        i = 0

        while i < len(meetings)-1:
            meeting1, meeting2 = meetings[i], meetings[i+1]
            if overlap(meeting1, meeting2):
                return False
            i+= 1
        return True
