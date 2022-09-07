from typing import List

# Runtime: 707 ms, faster than 96.64% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 27.9 MB, less than 77.89% of Python3 online submissions for Maximum Subarray.
# https://leetcode.com/submissions/detail/714636630/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """strat: Kadane's algorithm"""
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum += num
            if current_sum < num:
                current_sum = num
            max_sum = max(max_sum, current_sum)
        return max_sum


print(Solution().maxSubArray([-2, 1, -3, 2, -1, 4, 1, -5, 4]))
print(Solution().maxSubArray([1]))
