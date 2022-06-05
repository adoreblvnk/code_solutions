# Determine if String Halves Are Alike
# Runtime: 39 ms, faster than 82.91% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 13.8 MB, less than 98.41% of Python3 online submissions for Determine if String Halves Are Alike.
# https://leetcode.com/submissions/detail/714796669/

class Solution:
    def halvesAreAlike(self, s):
        return len([char for char in s[:len(s)//2] if char.lower() in "aeiou"]) == len([char for char in s[len(s)//2:] if char.lower() in "aeiou"])


print(Solution().halvesAreAlike("book"))
