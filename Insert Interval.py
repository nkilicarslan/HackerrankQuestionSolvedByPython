class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        flag_appending = False
        for index, intervals in enumerate(intervals):
            if newInterval[1] < intervals[0]:
                res.append(newInterval)
                return res + intervals[index:]
            elif newInterval[0] > intervals[1]:
                res.append(intervals)
            else:
                newInterval = [min(intervals[0], newInterval[0]), max(intervals[1], newInterval[1])]

        res.append(newInterval)
        return res
