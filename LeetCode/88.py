from typing import List

# Result:
# Runtime: 33 ms, faster than 95.44% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 39.06% of Python3 online submissions for Merge Sorted Array.
# https://leetcode.com/submissions/detail/701798004/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


print(Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
