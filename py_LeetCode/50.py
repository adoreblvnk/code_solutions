# Runtime: 28 ms, faster than 94.57% of Python3 online submissions for Pow(x, n).
# Memory Usage: 13.9 MB, less than 19.01% of Python3 online submissions for Pow(x, n).
# https://leetcode.com/submissions/detail/711232049/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))
