class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        print(intervals)

        lengthIntervals = len(intervals)
        count = 0


        if lengthIntervals < 2:
            return count

        prevStart, prevEnd = intervals[0]

        for i in range(1, lengthIntervals):

            currStart, currEnd = intervals[i]

            if prevEnd <= currStart:
                prevEnd = currEnd
                continue

            if currStart < prevEnd:
                count += 1
                prevEnd = min(prevEnd, currEnd)


        return count






        