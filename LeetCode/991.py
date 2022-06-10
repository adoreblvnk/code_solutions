# Broken Calculator

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        while startValue < target:
            if target % 2:
                target += 1
            else:
                target //= 2
            operations += 1
        return startValue - target + operations
      
print(Solution.()brokenCalc(2, 3))
