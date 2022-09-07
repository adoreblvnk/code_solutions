from typing import List

# Result:
# Runtime: 53 ms, faster than 81.24% of Python3 online submissions for Search Insert Position.
# Memory Usage: 14.8 MB, less than 6.74% of Python3 online submissions for Search Insert Position.
# https://leetcode.com/submissions/detail/704003069/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Strat: Binary Search"""
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if target > nums[mid]:
            return low
        return high + 1


print(Solution().searchInsert([2, 3, 5, 6], 1))
