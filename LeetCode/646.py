# Maximum Length of Pair Chain
# Runtime: 225 ms, faster than 87.67% of Python3 online submissions for Maximum Length of Pair Chain.
# Memory Usage: 14.6 MB, less than 8.97% of Python3 online submissions for Maximum Length of Pair Chain.
# https://leetcode.com/submissions/detail/715700802/

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """strat: memoization"""
        pairs.sort(key=lambda x: x[1])
        res = 1
        current = pairs[0]
        for i in range(1, len(pairs)):
            if current[1] < pairs[i][0]:
                res += 1
                current = pairs[i]
        return res


print(Solution().findLongestChain(
    [[-6, 9], [1, 6], [8, 10], [-1, 4], [-6, -2], [-9, 8], [-5, 3], [0, 3]]))
