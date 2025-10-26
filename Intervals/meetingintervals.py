# Definition for an interval.
from typing import List
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
       # Sort the intervals based on their start time
        intervals.sort(key=lambda x: x.start)
        # Check for overlaps
        for i in range (1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        # If no overlaps found, return True
        return True
