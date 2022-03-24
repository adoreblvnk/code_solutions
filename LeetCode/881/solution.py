from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]


print(Solution.findKthLargest("", [3, 2, 1, 5, 6, 4], 2))
