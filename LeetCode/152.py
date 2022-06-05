from typing import List

# Runtime: 89 ms, faster than 86.29% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14.3 MB, less than 78.07% of Python3 online submissions for Maximum Product Subarray.
# https://leetcode.com/submissions/detail/714769977/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """strat: Kadane's algorithm"""
        result = min_product = max_product = nums[0]
        for num in nums[1:]:
            max_product, min_product = max(
                num, max_product * num, min_product * num), min(num, max_product * num, min_product * num)
            result = max(max_product, result)
        return result


print(Solution().maxProduct([-2, -3, -4]))
