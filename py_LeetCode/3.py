# Result:
# Runtime: 63 ms, faster than 88.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 13.9 MB, less than 93.64% of Python3 online submissions for Longest Substring Without Repeating Characters.
# https://leetcode.com/submissions/detail/699895555/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        using sliding window technique
        """
        max_substr_len = start = 0
        char_map = {}
        for i, char in enumerate(s):
            if char in char_map and start <= char_map[char]:
                start = char_map[char] + 1
            else:
                max_substr_len = max(max_substr_len, i - start + 1)
            char_map[char] = i
        return max_substr_len


print(Solution().lengthOfLongestSubstring("tmmzuxt"))
