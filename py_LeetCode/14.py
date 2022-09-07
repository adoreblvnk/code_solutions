# Longest Common Prefix

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i, ch in enumerate(min(strs, key=len)):
            for other in strs:
                if other[i] != ch:
                    return strs[0][:i]
        return min(strs, key=len)


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
