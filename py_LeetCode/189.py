# Rotate Array
# Runtime: 213 ms, faster than 97.89% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.5 MB, less than 27.97% of Python3 online submissions for Rotate Array.
# https://leetcode.com/submissions/detail/736584590/

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]


print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
print(Solution().rotate([-1, -100, 3, 99], 2))
