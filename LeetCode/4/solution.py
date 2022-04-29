class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            res = (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
            return res
        else:
            res = nums1[len(nums1) // 2]
        return res

print(Solution.findMedianSortedArrays(Solution, [1, 3, 5], [2]))