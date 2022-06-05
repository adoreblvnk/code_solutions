from typing import List

# Runtime: 134 ms, faster than 86.77% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 14.6 MB, less than 49.39% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# https://leetcode.com/submissions/detail/714788083/


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        for i in range(1, len(nums)):
            if nums[i-1] >= nums[i]:
                operations += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1]+1
        return operations


print(Solution().minOperations([1, 5, 2, 4, 1]))
