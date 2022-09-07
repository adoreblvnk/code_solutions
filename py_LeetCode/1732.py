# Find the Highest Altitude

# https://leetcode.com/submissions/detail/761497825/
# Runtime: 37 ms, faster than 93.33% of Python3 online submissions for Find the Highest Altitude.
# Memory Usage: 13.8 MB, less than 54.37% of Python3 online submissions for Find the Highest Altitude.

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = cur_alt = 0
        for i in gain:
            cur_alt += i
            if cur_alt > max_alt:
                max_alt = cur_alt
        return max_alt


print(Solution().largestAltitude([-5, 1, 5, 0, -7]))
