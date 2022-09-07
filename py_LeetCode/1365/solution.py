from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(1 for j in nums if i > j) for i in nums]

    # solution
    def smallerNumbersThanCurrent_ans(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(a) for a in nums]


Solution.smallerNumbersThanCurrent_ans("", [8, 1, 2, 2, 3])
