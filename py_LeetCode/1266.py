from typing import List

# Results:
# Runtime: 60 ms, faster than 91.14% of Python3 online submissions for Minimum Time Visiting All Points.
# Memory Usage: 13.8 MB, less than 77.30% of Python3 online submissions for Minimum Time Visiting All Points.

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """strat: manhattan distance"""
        total_time = 0
        for i in range(len(points) - 1):
            total_time += max(abs(points[i][0] - points[i + 1][0]),
                              abs(points[i][1] - points[i + 1][1]))
        return total_time


print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
