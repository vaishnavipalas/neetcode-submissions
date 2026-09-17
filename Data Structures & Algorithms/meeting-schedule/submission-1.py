"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)

        if len(intervals) < 2:
            return True

        for i in range(1, len(intervals)):

            start_i = intervals[i].start

            prev_end = intervals[i-1].end

            if prev_end > start_i:
                return False

        return True