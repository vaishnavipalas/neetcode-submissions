class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = newInterval

        res = []

        added = False

        for start_i, end_i in intervals:

            if added:
                res.append([start_i, end_i])
                continue

            if end_i < start:
                res.append([start_i, end_i])

            elif end < start_i:
                res.append([start, end])
                res.append([start_i, end_i])
                added = True

            else:

                start = min(start, start_i)
                end = max(end, end_i)

        if not added:
            res.append([start, end])

        return res
        