# Regular Expression Matching
# Runtime: 70 ms, faster than 57.77% of Python3 online submissions for Regular Expression Matching.
# Memory Usage: 14.1 MB, less than 36.30% of Python3 online submissions for Regular Expression Matching.
# https://leetcode.com/submissions/detail/719366160/

import re


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if re.match(f"^{p}$", s) else False


print(Solution().isMatch("aa", "a"))
