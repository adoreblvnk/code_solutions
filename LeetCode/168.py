# Excel Sheet Column Title
# Runtime: 33 ms, faster than 85.73% of Python3 online submissions for Excel Sheet Column Title.
# Memory Usage: 13.9 MB, less than 54.68% of Python3 online submissions for Excel Sheet Column Title.
# https://leetcode.com/submissions/detail/730578253/

import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 0:
            columnNumber, rem = divmod(columnNumber-1, 26)
            s = string.ascii_uppercase[rem] + s
        return s


print(Solution().convertToTitle(1))
print(Solution().convertToTitle(26))
print(Solution().convertToTitle(701))
