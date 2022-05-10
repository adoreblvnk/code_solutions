# Result:
# Runtime: 32 ms, faster than 91.26% of Python3 online submissions for Reverse Words in a String.
# Memory Usage: 13.9 MB, less than 97.90% of Python3 online submissions for Reverse Words in a String.
# https://leetcode.com/submissions/detail/696803493/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])


print(Solution.reverseWords(Solution, "   a good   example   "))
