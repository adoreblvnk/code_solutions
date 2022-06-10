class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = sum(1 for i in nums if i == 0)
        white = sum(1 for i in nums if i == 1)
        blue = sum(1 for i in nums if i == 2)
        nums[:red] = [0] * red
        nums[red:red+white] = [1] * white
        nums[red+white:red+white+blue] = [2] * blue


Solution.sortColors("", nums=[2, 0, 2, 1, 1, 0])
