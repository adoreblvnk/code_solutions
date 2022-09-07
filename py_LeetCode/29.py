# Runtime: 24 ms, faster than 99.38% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 13.9 MB, less than 25.68% of Python3 online submissions for Divide Two Integers.
# https://leetcode.com/submissions/detail/710236166/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quot_abs = abs(dividend) // abs(divisor)
        ans = quot_abs * [-1, 1][dividend / divisor > 0]
        return min(ans, 2**31-1)

    def divide_v2(self, dividend: int, divisor: int) -> int:
        return min(abs(dividend) // abs(divisor) * [-1, 1][dividend / divisor > 0], 2**31-1)


print(Solution().divide(10, 3))
print(Solution().divide(-1, 1))
