from typing import List

# Runtime: 20 ms, faster than 99.87% of Python3 online submissions for Find Three Consecutive Integers That Sum to a Given Number.
# Memory Usage: 13.9 MB, less than 9.32% of Python3 online submissions for Find Three Consecutive Integers That Sum to a Given Number.


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        third = num // 3
        if num / 3 == third:
            return [third - 1, third, third + 1]
        return []


print(Solution.sumOfThree("", 33))
