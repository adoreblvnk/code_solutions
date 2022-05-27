# Result:
# Runtime: 38 ms, faster than 73.30% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.9 MB, less than 63.71% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        absolute = abs(x)
        reverse_int = 0
        while absolute > 0:
            reverse_int = reverse_int * 10 + absolute % 10
            absolute //= 10
            if reverse_int < -2**31 or reverse_int > 2**31 - 1:
                return 0
        return reverse_int * [-1, 1][x > 0]  # multiply by sign


print(Solution().reverse(123))
