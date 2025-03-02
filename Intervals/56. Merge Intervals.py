class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i in range(len(intervals)):
            last = ans[-1][1]
            if intervals[i][0] <= last:
                ans[-1][1] = max(last, intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans