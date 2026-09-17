class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        if len(intervals) < 2:
            return intervals

        res= []

        res.append(intervals[0])


        for i in range(1, len(intervals)):

            prev_start, prev_end = res[-1]

            curr_start, curr_end = intervals[i]

            if prev_end < curr_start:
                res.append(intervals[i])
            else:

                res[-1][1] = max(prev_end, curr_end)


        return res
        