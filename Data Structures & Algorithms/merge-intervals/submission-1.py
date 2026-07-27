class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        newray = []

        for rgt,lft in intervals:
            if not newray or rgt > newray[-1][1]:
                newray.append([rgt,lft])
            else:
                newray[-1][1] = max(newray[-1][1], lft)
        return newray