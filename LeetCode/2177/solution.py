from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        third = num // 3
        if num / 3 == third:
            return [third - 1, third, third + 1]
        return []


print(Solution.sumOfThree("", 33))
