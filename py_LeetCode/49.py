from typing import List
from collections import defaultdict

# Runtime: 101 ms, faster than 90.91% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.5 MB, less than 37.03% of Python3 online submissions for Group Anagrams.
# https://leetcode.com/submissions/detail/710152215/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        NOTE:
            defaultdict creates new key if not exists.
            hashmap to group sorted words together.
        """
        hashmap = defaultdict(list)
        for word in strs:
            hashmap[tuple(sorted(word))].append(word)
        return hashmap.values()


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
