# Backspace String Compare
# Runtime: 29 ms, faster than 95.55% of Python3 online submissions for Backspace String Compare.
# Memory Usage: 13.8 MB, less than 73.32% of Python3 online submissions for Backspace String Compare.
# https://leetcode.com/submissions/detail/718939075/

from collections import deque


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def _helper(text):
            result = deque()
            for i in text:
                if i != '#':
                    result.append(i)
                elif result:
                    result.pop()
                else:
                    continue
            return result
        return _helper(s) == _helper(t)


print(Solution().backspaceCompare("#a#c", "a##c"))
