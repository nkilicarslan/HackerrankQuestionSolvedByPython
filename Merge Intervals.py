class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        res.append(intervals[0])

        for new_interval in intervals[1:]:
            last_interval = res.pop()
            if new_interval[0] <= last_interval[1] and new_interval[1] >= last_interval[1]:
                res.append([last_interval[0], new_interval[1]])
            elif new_interval[0] >= last_interval[1]:
                res.append(last_interval)
                res.append(new_interval)
            elif new_interval[1] <= last_interval[1]:
                res.append(last_interval)

        return res