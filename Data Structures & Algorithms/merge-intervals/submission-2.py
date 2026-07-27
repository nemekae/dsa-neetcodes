class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        newray = [intervals[0]]

        for i in intervals:
            if i[0] <= newray[-1][1]:
                newray[-1][1] = max(newray[-1][1], i[1])
            else:
                newray.append(i)
        return newray