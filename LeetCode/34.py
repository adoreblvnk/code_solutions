from typing import List
from bisect import bisect_left, bisect_right

# Runtime: 94 ms, faster than 75.50% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 15.4 MB, less than 93.39% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# https://leetcode.com/submissions/detail/711240389/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [bisect_left(nums, target), bisect_right(nums, target) - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
print(Solution().searchRange([], 0))
